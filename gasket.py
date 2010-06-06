import Tkinter
import random
import time

class Sierpinski(object):
    '''A simple Sierpinski's Gasket viewer'''
    def __init__(self, width=400, height=400):
        #constrain width and height to numbers greater than 100
        width = max(width, 100)
        height = max(height, 100)
        
        #initialize the count
        self.count = 0
        
        #variables the user may wish to set
        #to control the display or speed
        pad = 10
        self.wait = 0.01
        self.iterations = 200
        
        #initialize the current point and the list of points in the triangle
        self.current = (width / 2, height / 2)
        self.points = [((width / 2, pad), 'red'),
                       ((pad, height - pad), 'green'),
                       ((width - pad, height - pad ), 'blue')]
        
        #initialize our widgets
        self._master = Tkinter.Tk()

        self._canvas = Tkinter.Canvas(self._master, width=width, height=height)
        self._canvas.pack()
        
        self._fast = Tkinter.Button(self._master, text='Fast', command=self._do_many_fast)
        self._fast.pack(side=Tkinter.LEFT, fill=Tkinter.X, expand=True)
        
        self._slow = Tkinter.Button(self._master, text='Slow', command=self._do_many_slow)
        self._slow.pack(side=Tkinter.LEFT, fill=Tkinter.X, expand=True)
        
        self._counter = Tkinter.Entry(self._master)
        self._counter.pack(side=Tkinter.LEFT, fill=Tkinter.X, expand=True)
        
        self._update_counter(0)
        
        #draw the triangle points
        for point,color in self.points:
            self._draw_dot(point,color)
    
    def _midpoint(self, (x1, y1), (x2, y2)):
        '''Return the point halfway between the given points'''
        return ((x1 + x2) / 2, (y1 + y2) / 2)
        
    def _draw_dot(self, (x, y), color):
        '''Draw a colored dot on the canvas, 
            since Tkinter.Canvas doesn't support coloring pixels
            we draw a very short line instead
        '''
        self._canvas.create_line(x, y, x + 1, y + 1, fill=color)
    
    def _update_counter(self, x):
        '''Increment the count and update the display'''
        self.count += x
        self._counter.delete(0,Tkinter.END)
        self._counter.insert(0,str(self.count))
    
    def _do_one(self):
        '''Process a single iteration:
            - Choose one of the original points at random
            - Move halfway between that point and the current location
            - Draw a dot the specified color
        '''
        point, color = random.choice(self.points)
        self.current = self._midpoint(self.current, point)
        self._draw_dot(self.current, color)
        
    def _do_many_fast(self):
        '''Iterate as fast as possible'''
        for i in xrange(self.iterations):
            self._do_one()
        self._update_counter(self.iterations)
    
    def _do_many_slow(self):
        '''Iterate with pauses to allow user to watch the changes and count by ones'''
        for i in xrange(self.iterations):
            time.sleep(self.wait)
            self._do_one()
            self._update_counter(1)
            #allow the display to update
            self._canvas.update_idletasks()
            
    def mainloop(self):
        '''Begin the Tkinter execution loop'''
        Tkinter.mainloop()

if __name__ == '__main__':
    S = Sierpinski()
    S.mainloop()
