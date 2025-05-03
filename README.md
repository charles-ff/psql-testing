# Private SQL CURL Request Script

## Google GCP and PrivateSQL Setup
For more details on this subject, please refer to our writeup. This process is quite involved and required support from Oasis Labs.

## Running the Script
- You firstly need to acquire your user specific JWT token. This is documented in PrivateSQL's documentation, but the commands are listed below as well:
  ``` bash
  curl -X POST -H "Content-Type: application/json" http://10.142.0.2/auth -d '{"id": <uuid>, "secret": <secret>}'
  ```
- You will then use the output of this command in line 11 of `psql.py`:
  ```python
  JWT = "<JWT>"  # replace this with your actual JWT
  ```
- Once an instance has been created for your specific public key/device, run this command to create a tunnel from your machine to the remote instance given to you by PrivateSQL.
  ``` bash
  ssh -L 9999:<IP of your instance>:80 username@remote-ip
  ```
- Example inputs and the function to run the inputs are shown below:
  ```python
  safe_aggregates = ["SELECT sex, COUNT(*) FROM medical_insurance GROUP BY sex",
                     "SELECT smoker, COUNT(*) FROM medical_insurance GROUP BY smoker",
                     "SELECT region, COUNT(*) FROM medical_insurance GROUP BY region"]
  run_queries(safe_aggregates)
  ```
- To run the code:
  ```bash
  python psql.py
  ```
