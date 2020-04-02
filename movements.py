import cv2

def move_to(customer,supermarket,target_y,target_x):
# up
    if target_y < customer.yx[0] and target_x is customer.yx[1]:
        while customer.yx[0]>target_y:
            customer.vv[0] = -1
            supermarket.draw()
            supermarket.render()
            customer.move()
            if cv2.waitKey(0) == ord('q'):
                break
# down
    elif target_y > customer.yx[0] and target_x is customer.yx[1]:
            while customer.yx[0]<target_y:
                customer.vv[0] = 1
                supermarket.draw()
                supermarket.render()
                customer.move()
                if cv2.waitKey(0) == ord('q'):
                    break
    # left
    elif target_x < customer.yx[1] and target_y is customer.yx[0]:
            while customer.yx[1]>target_x:
                customer.vv[1] = -1
                supermarket.draw()
                supermarket.render()
                customer.move()
                if cv2.waitKey(0) == ord('q'):
                    break
    # right
    else:
            while customer.yx[1]<target_x:
                customer.vv[1] = 1
                supermarket.draw()
                supermarket.render()
                customer.move()
                if cv2.waitKey(0) == ord('q'):
                    break
