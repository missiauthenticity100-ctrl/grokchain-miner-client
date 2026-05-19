import time
import random

print("Grokchain Miner Client")
print("Choose coin to mine:")
print("1. BTC-Pearl")
print("2. BTC-Black")
print("3. BTC-Platinum")

choice = input("Enter number: ")

if choice == "1":
    print("Mining BTC-Pearl (Agricultural task)...")
elif choice == "2":
    print("Mining BTC-Black (Water task)...")
elif choice == "3":
    print("Mining BTC-Platinum (Hunger grant task)...")

print("Mining in progress... (10-day block simulation)")
time.sleep(5)
print("Block mined! Reward sent to wallet.")
