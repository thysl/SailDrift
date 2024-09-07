# Code Organization

### We use a file per class system, with files grouped in packages. <br>
### The file system is as follows (expected):

- main.py
- /sails
    - \_\_init\_\_.py
    - mainsail.py
    - headsail.py
- /water_resistance
    - \_\_init\_\_.py
    - hull.py
    - keel.py
    - rudder.py
- /rendering
    - \_\_init\_\_.py
    - bkg_scroll.py
    - wake.py
- /datasets
    - \_\_init\_\_.py
    - sail_data.py
    - /boats
        - \_\_init\_\_.py
        - lelievlet.py
        - polyvalk.py
