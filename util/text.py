# Copyright (c) 2018 Chen-Ting Chuang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import cv2


def draw_text_in_box(frame, box_top, box_right, box_bottom, box_left,
                     font_face, font_scale, font_thickness,
                     text, text_color, fill_color):
    cv2.rectangle(frame, (box_left, box_top), (box_right, box_bottom),
                  fill_color, -1)

    text_size, baseline = cv2.getTextSize(text, font_face, font_scale, font_thickness)
    text_width, text_height = text_size[0], text_size[1]
    text_x = int(box_left + (box_right - box_left - text_width) / 2)
    text_y = int(box_top + (box_bottom - box_top - text_height) / 2) + text_height
    cv2.putText(frame, text, (text_x, text_y), font_face, font_scale,
                text_color, font_thickness)
