# Don-Dash

## Playing around with CloudPassage Halo API and Flask

### Never, EVER run this on a port accessible to other hosts on your LAN or WAN.  This tool requires a full-access key to initiate scans, and anyone hitting the (NOT HTTPS) web interface will be able to manipulate your account.


Set the following environment variables before you run the container.

| What it is                  | What it does                                                   |
|-----------------------------|----------------------------------------------------------------|
| HALO_API_KEY                | This is the API key for your Halo account.                     |
| HALO_API_SECRET_KEY         | This is the secret key for the Halo API.                       |
| HALO_API_HOSTNAME           | If in doubt, set this to ```api.cloudpassage.com```            |
| HALO_API_PORT               | If in doubt, set this to ```443```                             |
| HALO_AGENT_KEY              | This is the agent registration key for your account.           |
| SERVER_GROUP                | This is the server tag, which ensures correct group assignment |


Building and running:

* `docker build -t dondash .`
* `docker run -it --rm -e HALO_API_KEY=$HALO_API_KEY -e HALO_API_SECRET_KEY=$HALO_API_SECRET_KEY -e HALO_API_HOSTNAME=$HALO_API_HOSTNAME -e HALO_API_PORT=$HALO_API_PORT -e HALO_AGENT_KEY=$HALO_AGENT_KEY -e SERVER_GROUP=$SERVER_GROUP -p 5000:5000 dondash`

Running without overriding the container's CMD (putting nothing after dondash) only requires read-only keys.  Also, it runs only the web app, *not* the Halo agent.

If you override the default CMD with `/app/scan_with_halo.sh`, you will cause the Halo agent to start, and a script will tell the grid to initiate CSM and SVM scans against the image.  When the scans are finished, it pretty-prints the scan results to stdout.

If you override the default CMD with `/app/run_with_halo.sh`, you'll run the application *and* the Halo agent in the container.
