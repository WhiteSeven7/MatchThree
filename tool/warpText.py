def wrap_text(text, font, max_width):
    line_text: list[str] = []
    begin = 0
    for end in range(1, len(text) + 1):
        if font.render(text[begin:end + 1], True, 'black').get_width() > max_width:
            line_text.append(text[begin:end])
            begin = end
    line_text.append(text[begin:])
    return line_text


"""
a = [0,1,2,3,4,5,6]
len(a) = 7
range(1, len(a) + 1) = range(1, 8) ~= [1,2,3,4,5,6,7]
a[4:7] = [a[4],a[5],a[6]]

range(1, len(text) + 1) = range(1, 7 + 1)
end = 1
end = 2
end = 3
font.render(text[0:3 + 1], True, 'black').get_width() > max_width
line_text.append(text[0:3]) 0,1,2
begin = end = 3
end = 4
end = 5
font.render(text[0:5 + 1], True, 'black').get_width() > max_width
line_text.append(text[3:5]) 3,4
begin = end = 5
end = 6
end = 7
line_text.append(text[5:()])

"""
