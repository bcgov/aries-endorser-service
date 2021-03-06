# Aries - Endorser Service

This repository provides an Endoser agent, based on [Aries Cloudagent Pythong (or Aca-Py)](https://github.com/hyperledger/aries-cloudagent-python).

Information about Aca-Py's Endorser support can be found [here](https://github.com/hyperledger/aries-cloudagent-python/blob/main/Endorser.md).

The Aca-Py Alice/Faber demo also demonstrates the use of the Endorser feature, as described [here](https://github.com/hyperledger/aries-cloudagent-python/blob/main/demo/Endorser.md).

This repository is a work in progress, see [this document](https://hackmd.io/hWMLdpu7SBuopNag4mTbcg?view) for the on-going requirements and design.

## Running Locally

To get up and running quicky, open a bash shell and run the following:

```bash
git clone https://github.com/bcgov/aries-endorser-service.git
cd aries-endorser-service/docker
./manage build
./manage start --logs
```

To shut down the service:

```bash
<ctrl-c>
./manage rm
```

By default, the Endorser runs against the BCovrin Test ledger (http://test.bcovrin.vonx.io/).  To run against a different ledger, start using the `GENESIS_URL` parameter:

```bash
GENESIS_URL=<path to genesis txn> ./manage start --logs
```

For example, the SOVRIN staging ledger's transactions can be found [here](https://raw.githubusercontent.com/sovrin-foundation/sovrin/master/sovrin/pool_transactions_sandbox_genesis).

By default, the `./manage` script will use a random seed to generate the Endorser's public DID.  Author agents will need to know this public DID in order to create transactions for endorsement.  If you need to start the Endorser using a "well known DID" you can start with the `ENDORSER_SEED` parameter:

```bash
ENDORSER_SEED=<your 32 char seed> ./manage start --logs
```

## Testing

There are currently no unit or integration tests in this repository.  However you can test using [traction](https://github.com/bcgov/traction).

Open a bash shell and startup the endorser services:

```bash
git clone https://github.com/bcgov/aries-endorser-service.git
cd aries-endorser-service/docker
./manage build
# note we start with a "known" endorser DID
ENDORSER_SEED=testendorserseed_123123123123123 ./manage start --logs
```

Then open a separate bash shell and run the following:

```bash
git clone https://github.com/bcgov/traction.git
cd traction/scripts
git checkout endorser-integration
cp .env-example .env
docker-compose build
docker-compose up
```

Then open up yet another bash shell and run the traction integration tests.  Traction tenants will connect to the endorser service for creating schemas, credential definitions etc.

```bash
cd <traction/scripts directory from above>
docker exec scripts_traction-api_1 pytest --asyncio-mode=strict -m integtest
```

... or you can run individual tests like this:

```bash
docker exec scripts_traction-api_1 pytest --asyncio-mode=strict -m integtest tests/integration/endpoints/routes/test_tenant.py::test_tenant_issuer
```

Traction integration tests create new tenants for each test, so you can rebuild/restart the endorser service without having to restart traction.
