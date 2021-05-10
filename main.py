class Body:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def get_magnitudes(self, time):
        final_velocity = self.velocity + self.acceleration * time
        final_position = self.position + ((self.velocity + final_velocity) * time * 0.5)
        return (final_position, final_velocity, self.acceleration)

def main():
    import sys

    if len(sys.argv) == 1:
        print('Usage:', sys.argv[0], '[m:magnitudes|h:help] [position] [velocity] [acceleration]')
    elif sys.argv[1] == 'h' or sys.argv[1] == 'help':
        print('Create a grap of position, velocity, acceleration with "', sys.argv[0], 'm (position) (velocity) (acceleration)"')
    elif (sys.argv[1] == 'm' or sys.argv[1] == 'magnitudes') and len(sys.argv) == 5:
        body = Body(float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))

        import drawing
        drawing.start_drawing(body)
    else:
        print('Usage:', sys.argv[0], '[m:magnitudes|h:help] [position] [velocity] [acceleration]')

if __name__ == '__main__':
    main()