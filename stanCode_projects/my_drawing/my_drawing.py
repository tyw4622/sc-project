"""
File: my_drawing.py
Name: Karen Wong
----------------------
This file uses campy module to
draw a figure on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    This program shows a drawing of tiger by using GPolygon in campy library.
    Watching Tiger King trailer on Netflix brings me the idea of this work.
    """
    window = GWindow(width=1000, height=800, title='my_drawing_tiger.py')
    
    # Face
    face = GPolygon()
    face.add_vertex((315, 317))
    face.add_vertex((327, 436))
    face.add_vertex((315, 496))
    face.add_vertex((408, 537))
    face.add_vertex((408, 482))
    face.add_vertex((449, 442))
    face.add_vertex((472, 322))
    face.add_vertex((435, 253))
    face.add_vertex((510, 207))
    face.add_vertex((585, 243))
    face.add_vertex((509, 372))
    face.add_vertex((568, 442))
    face.add_vertex((609, 482))
    face.add_vertex((609, 537))
    face.add_vertex((701, 490))
    face.add_vertex((670, 443))
    face.add_vertex((701, 311))
    face.add_vertex((659, 264))
    face.add_vertex((634, 242))
    face.add_vertex((593, 223))
    face.add_vertex((551, 210))
    face.add_vertex((500, 206))
    face.add_vertex((471, 209))
    face.add_vertex((408, 226))
    face.add_vertex((378, 247))
    face.add_vertex((355, 264))
    face.add_vertex((315, 317))
    face.filled = True
    face.fill_color = 'darkorange'
    face.color = 'darkorange'
    window.add(face)

    face_w = GPolygon()
    face_w.add_vertex((568, 442))
    face_w.add_vertex((609, 482))
    face_w.add_vertex((609, 577))
    face_w.add_vertex((574, 611))
    face_w.add_vertex((510, 581))
    face_w.add_vertex((441, 611))
    face_w.add_vertex((408, 575))
    face_w.add_vertex((408, 482))
    face_w.add_vertex((449, 442))
    face_w.filled = True
    face_w.fill_color = 'ivory'
    face_w.color = 'lightgray'
    window.add(face_w)

    face_r_b = GPolygon()
    face_r_b.add_vertex((670, 288))
    face_r_b.add_vertex((670, 317))
    face_r_b.add_vertex((640, 445))
    face_r_b.add_vertex((619, 443))
    face_r_b.add_vertex((648, 462))
    face_r_b.add_vertex((685, 317))
    face_r_b.filled = True
    window.add(face_r_b)

    face_l_b_p = GPolygon()
    face_l_b_p.add_vertex((350, 288))
    face_l_b_p.add_vertex((332, 317))
    face_l_b_p.add_vertex((367, 462))
    face_l_b_p.add_vertex((397, 445))
    face_l_b_p.add_vertex((378, 443))
    face_l_b_p.add_vertex((343, 317))
    face_l_b_p.filled = True
    window.add(face_l_b_p)

    face_l_b = GPolygon()
    face_l_b.add_vertex((315, 496))
    face_l_b.add_vertex((350, 443))
    face_l_b.add_vertex((320, 317))
    face_l_b.add_vertex((327, 436))
    face_l_b.filled = True
    window.add(face_l_b)

    face_l_b1 = GPolygon()
    face_l_b1.add_vertex((699, 317))
    face_l_b1.add_vertex((670, 443))
    face_l_b1.add_vertex((701, 490))
    face_l_b1.add_vertex((692, 443))
    face_l_b1.filled = True
    window.add(face_l_b1)

    face_rty = GPolygon()
    face_rty.add_vertex((699, 353))
    face_rty.add_vertex((692, 443))
    face_rty.add_vertex((700, 496))
    face_rty.add_vertex((751, 467))
    face_rty.filled = True
    face_rty.fill_color = 'gold'
    face_rty.color = 'gold'
    window.add(face_rty)

    face_lty = GPolygon()
    face_lty.add_vertex((321, 353))
    face_lty.add_vertex((269, 473))
    face_lty.add_vertex((315, 496))
    face_lty.add_vertex((327, 436))
    face_lty.filled = True
    face_lty.fill_color = 'gold'
    face_lty.color = 'gold'
    window.add(face_lty)

    face_r_t = GPolygon()
    face_r_t.add_vertex((659, 476))
    face_r_t.add_vertex((670, 490))
    face_r_t.add_vertex((634, 504))
    face_r_t.filled = True
    window.add(face_r_t)

    face_r_t1 = GPolygon()
    face_r_t1.add_vertex((701, 490))
    face_r_t1.add_vertex((688, 524))
    face_r_t1.add_vertex((609, 537))
    face_r_t1.filled = True
    window.add(face_r_t1)

    face_l_t = GPolygon()
    face_l_t.add_vertex((359, 476))
    face_l_t.add_vertex((350, 488))
    face_l_t.add_vertex((384, 504))
    face_l_t.filled = True
    window.add(face_l_t)

    face_l_t1 = GPolygon()
    face_l_t1.add_vertex((321, 499))
    face_l_t1.add_vertex((408, 537))
    face_l_t1.add_vertex((327, 524))
    face_l_t1.filled = True
    window.add(face_l_t1)
    
    # Chin
    chin = GPolygon()
    chin.add_vertex((441, 611))
    chin.add_vertex((510, 599))
    chin.add_vertex((574, 611))
    chin.add_vertex((574, 636))
    chin.add_vertex((510, 666))
    chin.add_vertex((441, 636))
    chin.filled = True
    chin.fill_color = 'whitesmoke'
    chin.color = 'silver'
    window.add(chin)
    
    # Nose
    nose = GPolygon()
    nose.add_vertex((510, 207))
    nose.add_vertex((435, 253))
    nose.add_vertex((472, 322))
    nose.add_vertex((435, 524))
    nose.add_vertex((507, 541))
    nose.add_vertex((585, 524))
    nose.add_vertex((546, 332))
    nose.add_vertex((585, 243))
    nose.filled = True
    nose.fill_color = 'gold'
    nose.color = 'gold'
    window.add(nose)

    nose1 = GPolygon()
    nose1.add_vertex((435, 524))
    nose1.add_vertex((510, 581))
    nose1.add_vertex((585, 524))
    nose1.add_vertex((507, 541))
    nose1.filled = True
    nose1.fill_color = 'saddlebrown'
    nose1.color = 'saddlebrown'
    window.add(nose1)

    nose_b_t = GPolygon()
    nose_b_t.add_vertex((510, 581))
    nose_b_t.add_vertex((441, 611))
    nose_b_t.add_vertex((510, 599))
    nose_b_t.add_vertex((574, 611))
    nose_b_t.filled = True
    window.add(nose_b_t)

    nose_b = GPolygon()
    nose_b.add_vertex((435, 238))
    nose_b.add_vertex((441, 257))
    nose_b.add_vertex((509, 238))
    nose_b.add_vertex((577, 257))
    nose_b.add_vertex((585, 243))
    nose_b.add_vertex((509, 238))
    nose_b.filled = True
    window.add(nose_b)

    nose_b1 = GPolygon()
    nose_b1.add_vertex((423, 278))
    nose_b1.add_vertex((435, 293))
    nose_b1.add_vertex((505, 264))
    nose_b1.add_vertex((585, 293))
    nose_b1.add_vertex((593, 277))
    nose_b1.add_vertex((505, 264))
    nose_b1.filled = True
    window.add(nose_b1)

    nose_b2 = GPolygon()
    nose_b2.add_vertex((441, 311))
    nose_b2.add_vertex((448, 322))
    nose_b2.add_vertex((509, 288))
    nose_b2.add_vertex((571, 322))
    nose_b2.add_vertex((579, 310))
    nose_b2.add_vertex((509, 288))
    nose_b2.filled = True
    window.add(nose_b2)

    nose_b3 = GPolygon()
    nose_b3.add_vertex((464, 348))
    nose_b3.add_vertex((455, 336))
    nose_b3.add_vertex((505, 317))
    nose_b3.add_vertex((560, 338))
    nose_b3.add_vertex((555, 348))
    nose_b3.add_vertex((505, 317))
    nose_b3.filled = True
    window.add(nose_b3)
    
    # Eyes
    l_eye_y = GPolygon()
    l_eye_y.add_vertex((395, 332))
    l_eye_y.add_vertex((370, 379))
    l_eye_y.add_vertex((428, 453))
    l_eye_y.add_vertex((435, 400))
    l_eye_y.add_vertex((459, 379))
    l_eye_y.filled = True
    l_eye_y.fill_color = 'beige'
    l_eye_y.color = 'beige'
    window.add(l_eye_y)

    l_eye_b = GPolygon()
    l_eye_b.add_vertex((370, 379))
    l_eye_b.add_vertex((459, 379))
    l_eye_b.add_vertex((435, 400))
    l_eye_b.filled = True
    window.add(l_eye_b)

    r_eye_y = GPolygon()
    r_eye_y.add_vertex((560, 379))
    r_eye_y.add_vertex((585, 400))
    r_eye_y.add_vertex((585, 453))
    r_eye_y.add_vertex((648, 379))
    r_eye_y.add_vertex((623, 332))
    r_eye_y.filled = True
    r_eye_y.fill_color = 'beige'
    r_eye_y.color = 'beige'
    window.add(r_eye_y)

    r_eye = GPolygon()
    r_eye.add_vertex((560, 379))
    r_eye.add_vertex((648, 379))
    r_eye.add_vertex((585, 400))
    r_eye.filled = True
    window.add(r_eye)
    
    # Ears
    r_ear = GPolygon()
    r_ear.add_vertex((634, 242))
    r_ear.add_vertex((659, 264))
    r_ear.add_vertex((707, 201))
    r_ear.filled = True
    window.add(r_ear)

    r_ear_y = GPolygon()
    r_ear_y.add_vertex((701, 311))
    r_ear_y.add_vertex((659, 264))
    r_ear_y.add_vertex((707, 201))
    r_ear_y.add_vertex((728, 213))
    r_ear_y.add_vertex((756, 256))
    r_ear_y.add_vertex((751, 278))
    r_ear_y.add_vertex((736, 293))
    r_ear_y.filled = True
    r_ear_y.fill_color = 'gold'
    r_ear_y.color = 'gold'
    window.add(r_ear_y)

    l_ear_y = GPolygon()
    l_ear_y.add_vertex((308, 195))
    l_ear_y.add_vertex((355, 264))
    l_ear_y.add_vertex((315, 317))
    l_ear_y.add_vertex((299, 305))
    l_ear_y.add_vertex((274, 287))
    l_ear_y.add_vertex((262, 264))
    l_ear_y.add_vertex((285, 219))
    l_ear_y.filled = True
    l_ear_y.fill_color = 'gold'
    l_ear_y.color = 'gold'
    window.add(l_ear_y)

    l_ear = GPolygon()
    l_ear.add_vertex((355, 264))
    l_ear.add_vertex((378, 247))
    l_ear.add_vertex((308, 195))
    l_ear.filled = True
    window.add(l_ear)


if __name__ == '__main__':
    main()
