import LibLathe.LLBaseOP
from LibLathe.LLPoint import Point
from LibLathe.LLSegment import Segment

class FaceOP(LibLathe.LLBaseOP.BaseOP):
    
    def generate_path(self):
        '''
        Generate the path for the profile operation
        '''
        xmin = self.stock.XMin - self.extra_dia 
        zmax = self.stock.ZMax + self.start_offset            
        
        self.clearing_paths = []
        length = zmax - self.part.ZMax
        #width = self.stock.XLength/2 - self.min_dia + self.extra_dia 
        step_over = self.step_over
        line_count = length / step_over

        print('line count', line_count)
           
        counter = 0
        while counter < line_count:
            zpt = zmax - counter * self.step_over

            print('zpt:', zpt)

            pt1 = Point(xmin, 0 , zpt)
            pt2 = Point(0 , 0 , zpt)
            path_line = Segment(pt1, pt2)

            '''
              
            roughing_boundary = self.offset_edges[-1]
            
            for seg in roughing_boundary:
                #if roughing_boundary.index(seg) == 0:
                #print(roughing_boundary.index(seg), counter)
                intersect, point = seg.intersect(path_line) 
                if intersect:
                    if type(point) is list:
                        point = pt1.nearest(point)
                    path_line = Segment(pt1, point)
                    #if utils.online(seg, point):
                    #    path_line = Segment(pt1, point)
                        
                        #break
            '''
            self.clearing_paths.append(path_line)
            counter += 1
 
        #clearing_lines = Part.makeCompound(self.clearing_paths)
        #Part.show(clearing_lines, 'clearing_path')
        





