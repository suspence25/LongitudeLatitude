import gmplot

gma_one = gmplot.GoogleMapPlotter(38.1833986,-85.6830407,12)
gma_one.draw('map.html')

gma_two = gma_one.heatmap()

exit()

def comma_rep(address):
    address = address.replace(',','')
    return address

address = [
    '401 Bullitt Ln, Louisville, KY 40222',
  
]

start_url = 'https://www.google.com/maps/place/'

#for a in address:

    # aa = a.replace(',','')
    # aaa = aa.replace(' ', '+')
    # print(aaa)
    # address_url = start_url + aaa
    # print('address_url: {}'.format(address_url))
    # get_current_url = 'https://www.google.com/maps/place/401+Bullitt+Ln,+Louisville,+KY+40222/@38.2457639,-85.6207408,17z/data=!3m1!4b1!4m5!3m4!1s0x88697546032f45c1:0x60b94806ec3fd23b!8m2!3d38.2457639!4d-85.6185521'
    # current_url = comma_rep(get_current_url)
    # print(current_url)
    # cur_url = current_url.replace(address_url, '')
    # print('cur_url: {}'.format(cur_url))
    # #Clean up
    # cur_url_1 = cur_url.split('z/data')[0]
    # cur_url_2 = cur_url_1.lstrip('/@')
    # print(cur_url_2)
    #add to new adddress for Verification







