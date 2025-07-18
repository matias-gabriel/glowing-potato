class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # [-5, 5, 10, 10, -20, 30]
        # last_negative = True
        # [ -5, 5, 10, 10, -20 ]
        # [-5,-20]
        stack = []
        last_negative = True
        for asteroid in asteroids:
            if not last_negative and asteroid < 0:
                while True:
                    if not stack:
                        last_negative = asteroid < 0 
                        stack.append(asteroid)
                        break

                    current = stack.pop()

                    if current < 0:
                        last_negative = True
                        stack.append(current)
                        stack.append(asteroid)
                        break
                        
                    p_asteroid = asteroid * -1

                    if current == p_asteroid:
                        break
                    elif current < p_asteroid:
                        continue
                    else:
                        stack.append(current)
                        break
            else:
                last_negative = asteroid < 0
                stack.append(asteroid)


        return stack
        