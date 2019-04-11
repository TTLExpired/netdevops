class MyDevice():
    ''' A networking device piece of code '''
    def __init__(self, vendor, module, slots, vlans):
        ''' What is the vendor, make and number of switches '''
        self.vendor = vendor
        self.module = module
        self.slots = int(slots)
        self.xvlans = int(vlans)
        self.vlans = {}

    def radius_key(self):
        ''' Radius Key '''
        self.radius = input('Radius Key? ')

    def vlan_data(self):
        ''' Vlans, names and IDs '''
        for i in range(self.xvlans):
            vname = input('Name? ')
            vid = int(input('ID? '))
            self.vlans[vname] = vid

    def return_vlans(self):
        for k, v in self.vlans.items():
            print(k, v)