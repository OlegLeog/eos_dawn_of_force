import requests, time

def dawn_of_force():
    print("EOS — The Force Just Awakened (100k+ EOS staked to a new account in one breath)")
    seen = set()
    while True:
        r = requests.get("https://eos.greymass.com/v1/history/get_actions?limit=50&account=eosio.stake")
        for act in r.json().get("actions", []):
            h = act["action_trace"]["trx_id"]
            if h in seen: continue
            seen.add(h)

            data = act["action_trace"]["act"]["data"]
            if not data.get("to"): continue
            amount = int(data.get("stake_net_quantity", "0").split()[0]) + int(data.get("stake_cpu_quantity", "0").split()[0])
            if amount > 100_000:  # >100k EOS delegated in one action
                receiver = data["to"]
                print(f"THE FORCE AWAKENS\n"
                      f"{amount:,.0f} EOS just granted superhuman power\n"
                      f"To: {receiver}\n"
                      f"From: {data['from']}\n"
                      f"Tx: https://bloks.io/transaction/{h}\n"
                      f"→ A new entity just received god-tier bandwidth\n"
                      f"→ They can now run dApps that eat entire chains for breakfast\n"
                      f"→ EOS just crowned a new titan\n"
                      f"{'⚡'*55}\n")
        time.sleep(2.1)

if __name__ == "__main__":
    dawn_of_force()
