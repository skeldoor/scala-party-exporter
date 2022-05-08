import urllib.request, json

domainName = "scala.party"
path = "/api/live_stats"
url = "https://" + domainName + path


def hashesToKilohashes(hashes):
    return hashes / 1000

def hashesToKilohashesSting(hashes):
    kilohashes = hashesToKilohashes(hashes)
    return str(kilohashes)

def main():
    with urllib.request.urlopen(url) as webpage:
        data = json.loads(webpage.read().decode())
        print(data)
        hashrate = data["pool"]["hashrate"]
        miners = data["pool"]["miners"]
        workers = data["pool"]["workers"]
        print( "Hashrate: " + hashesToKilohashesSting(hashrate) + "KH/s" )
        print( "Miners: " + str(miners) )
        print( "Workers: " + str(workers))

if __name__ == "__main__":
    main()