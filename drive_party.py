
##Import local library explore: see explore.py
import gpio_cleanup
import explore


for z in range(20):
    explore.mode_discovery(2, 2.00, 'party', 'on')

print("\n\nFinished drive_party\n\nrun me again!")
