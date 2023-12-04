import folium
from folium.plugins import HeatMap

def create_legend(map):
    legend_img = './legend_file.png'

    legend_html = '''
         <div style="position: fixed; 
                     bottom: 50px; left: 50px; width: 75px; height: auto; 
                     z-index:9999; font-size:14px;
                     ">
                      <img src="{}" alt="legend" style="width:75px;height:auto;">
         </div>
         '''.format(legend_img)

    map.get_root().html.add_child(folium.Element(legend_html))


def heatmap(data, max_geo_count=1, legend=False):
    map = folium.Map(location=[39.29,-76.616], zoom_start=13, tiles='https://api.mapbox.com/styles/v1/eddieleee/clppws70800nx01p87des5rxr/tiles/256/{z}/{x}/{y}@2x?access_token=sk.eyJ1IjoiZWRkaWVsZWVlIiwiYSI6ImNscHE1amk3eDE0djcycHBndjY5ZG1nZTcifQ.emv8CS-Hd4z837in-SHOeA',attr='Mapbox')

    HeatMap(data, gradient={0.15: 'blue', 0.23: "#1b6d92", 0.3: 'lime', 0.36:"#84e11e", 0.39: "#adeb14", 0.45: 'yellow', 0.51:"#ffd300", 0.57:"#ffa600", 0.64:"#ff7200", 0.7: 'orange', 1: 'red'},
            min_opacity=0.1, max_opacity=0.95,
            max_val = max_geo_count*0.9,
            radius=25, blur=15,max_zoom=1).add_to(map)
    if legend:
        create_legend(map)

    map.save('baltimore_heatmap.html')