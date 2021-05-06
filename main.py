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
    body = Body(0, 5, -1)

    for time in range(100):
        magnitudes = body.get_magnitudes(time)
        print(magnitudes)

if __name__ == '__main__':
    main()