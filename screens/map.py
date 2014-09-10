from screens.base import Base


class Map(Base):
    map_area = ('class_name', 'UIAMapView')
    current_location = ('id', 'Current Location')

    def pan_map_area(self):
        self.wait_visible(self.map_area)
        map_area_attributes = self.get_element_attributes(self.map_area)
        self.driver.swipe(
            map_area_attributes['center_x'],
            map_area_attributes['top'] + 1,
            map_area_attributes['center_x'],
            map_area_attributes['bottom'] - 1
        )
