try:
    raise ZeroDivisionError('its not correct division')
    z=1/0
    print(z)
except ZeroDivisionError as e:
    print(e)
finally:
    print('program execution completed')
