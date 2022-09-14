import os
import sys
upHostsFilename = "upHosts.txt"
#iterate through list of hosts and ping to see if up then add to list of confirmed up hosts
def ping(host):
    #ping host
    try:
        response = os.popen(f"ping -c 2 {host}").read()
        if "Received = 4" in response:
            return False
        else:
            return True
    except Exception:
            return False
def main():
    #iterate through list of hosts to ping from file passed in argument
    with open(sys.argv[1]) as f:
        for line in f:
            #clear the line of new line character
            host = line.strip()
            if ping(host):
                #write host to upHostsFilename
                with open(upHostsFilename, "a") as f:
                    f.write(host + "\n")
                with open(upHostsFilename) as f:
                    print("Number of up hosts: " + str(len(f.readlines())))


if __name__ == "__main__":
    main()