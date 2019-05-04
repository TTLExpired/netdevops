class MyDevice:
    ''' sample class for network devices '''
    def __init__(self, router_ip, switches_ip=''):
        self.router_ip = router_ip
        if switches_ip:
            self.switches_ip = switches_ip

    def is_router(self):
        print('router ID is ', self.router_ip)

    def is_switches(self):
        if self.switches_ip:
            for switch in self.switches_ip:
                print('switches are: ')
                print(switch)
        else:
            print('No swtiches!')

    def add_switch(self, ip_address):
        self.switches_ip.append(ip_address)

    def rm_switch(self, ip_address):
        self.switches_ip.remove(ip_address)

    def add_driver(self, driver):
        self.driver = driver

    def what_driver(self):
        print('Driver is ', self.driver)


def main():
    ''' A small script to figur out MAC tp IP '''
    router_ip = input('Enter Router ID: ')
    switches_ip = input("Enter Switches with ',' in between").split(',')

    # Let's build the first object
    device = MyDevice(router_ip, switches_ip)
    device.is_router()
    device.is_switches()


if __name__ == '__main__':
    main()