from napalm import get_network_driver

import json


def main():
        '''Get some bgp data and save to a csv file'''

        # First, get list of devices
        devices = ['10.47.254.252', '10.47.254.251',
                   '10.0.7.254', '10.0.7.253']

        # iosxr driver
        xr_driver = get_network_driver('iosxr')
        ios_driver = get_network_driver('ios')

        # Some variables
        remote_as = 'remote_as'
        router_id = 'router_id'
        state = 'connection_state'
        flap = 'flap_count'
        rx_route = 'accepted_prefix_count'
        tx_route = 'advertised_prefix_count'

        # Initiate a list
        list_bgp_data = []

        # Get data
        for device in devices:
                if '10.47' in device:
                        with xr_driver(device, 'LastResort', 'RaY13M07') as wan:
                                bgp_data = wan.get_bgp_neighbors_detail()
                                list_bgp_data.append(bgp_data)
                else:
                        with ios_driver(device, 'LastResort', 'RaY13M07') as wan:
                                bgp_data = wan.get_bgp_neighbors_detail()
                                list_bgp_data.append(bgp_data)

        header = 'router_id,remote_as,received_routes,transmit_routes,state,flap'

        with open('bgpdata.csv', 'a') as f:
                f.write(header + '\n')

        print(header)
        for bgp_data in list_bgp_data:
                for key, value in bgp_data.items():
                        for nkey, nvalue in value.items():
                                for data in nvalue:
                                        # print(str(data[router_id]) + ',' +
                                        #       str(data[remote_as]) + ',' +
                                        #       str(data[rx_route]) + ',' +
                                        #       str(data[tx_route]) + ',' +
                                        #       str(data[state]) + ',' +
                                        #       str(data[flap]))

                                        with open('bgpdata.csv', 'a') as f:
                                                f.write(str(data[router_id]) + ',' +
                                                        str(data[remote_as]) + ',' +
                                                        str(data[rx_route]) + ',' +
                                                        str(data[tx_route]) + ',' +
                                                        str(data[state]) + ',' +
                                                        str(data[flap]) + '\n')


if __name__ == '__main__':
        main()
