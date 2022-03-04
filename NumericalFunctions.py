from math import floor


def Binary_to_Decimal(Binary):
    Decimal_point = Binary.find('.')
    if Decimal_point >= 0:
        int_part = Binary[:Decimal_point]
        dec_part = Binary[Decimal_point+1:]
        for i in int_part:
            if i != '1' and i != '0':
                result = i + 9.01
        for i in dec_part:
            if i != '1' and i != '0':
                result = i + 9.01
        int_part = int_part[::-1]
        j = 0
        result = 0
        for i in int_part:
            result += int(i) * (2 ** j)
            j += 1
        k = -1
        for i in dec_part:
            result += int(i) * (2 ** k)
            k -= 1
        return result
    else:
        int_part = Binary[::-1]
        for i in int_part:
            if i != '1' and i != '0':
                result = i + 9.01
        j = 0
        result = 0
        for i in int_part:
            result += int(i) * (2 ** j)
            j += 1
        return result


def Octal_to_Decimal(Octal):
    Decimal_point = Octal.find('.')
    if Decimal_point >= 0:
        int_part = Octal[:Decimal_point]
        dec_part = Octal[Decimal_point + 1:]
        for i in int_part:
            int(i)
        for i in dec_part:
            int(i)
        int_part = int_part[::-1]
        j = 0
        result = 0
        for i in int_part:
            result += int(i) * (8 ** j)
            j += 1
        k = -1
        for i in dec_part:
            result += int(i) * (8 ** k)
            k -= 1
        return result
    else:
        int_part = Octal[::-1]
        for i in int_part:
            int(i)
        j = 0
        result = 0
        for i in int_part:
            result += int(i) * (8 ** j)
            j += 1
        return result


def Hexadecimal_to_Decimal(Hexadecimal):
    Decimal_point = Hexadecimal.find('.')
    Hexadecimal_Conversions = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    if Decimal_point >= 0:
        int_part = Hexadecimal[:Decimal_point]
        dec_part = Hexadecimal[Decimal_point + 1:]
        for i in int_part:
            if i.isalpha():
                if i in Hexadecimal_Conversions:
                    continue
                else:
                    error = i + 10
        for i in dec_part:
            if i.isalpha():
                if i in Hexadecimal_Conversions:
                    continue
                else:
                    error = i + 10
        int_part = int_part[::-1]
        j = 0
        result = 0
        for i in int_part:
            if i in Hexadecimal_Conversions:
                i = Hexadecimal_Conversions[i]
            result += int(i) * (16 ** j)
            j += 1
        k = -1
        for i in dec_part:
            if i in Hexadecimal_Conversions:
                i = Hexadecimal_Conversions[i]
            result += int(i) * (16 ** k)
            k -= 1
        return result
    else:
        int_part = Hexadecimal[::-1]
        for i in int_part:
            if i.isalpha():
                if i in Hexadecimal_Conversions:
                    continue
                else:
                    error = i + 10
        j = 0
        result = 0
        for i in int_part:
            if i in Hexadecimal_Conversions:
                i = Hexadecimal_Conversions[i]
            result += int(i) * (16 ** j)
            j += 1
        return result


def Decimal_to_Binary(Decimal):
    Decimal_point = Decimal.find('.')
    if Decimal_point >= 0:
        if Decimal_point == 0:
            int_part = '0'
            dec_part = Decimal[Decimal_point + 1:]
        else:
            int_part = Decimal[:Decimal_point]
            dec_part = Decimal[Decimal_point + 1:]
        for i in int_part:
            if i.isalpha():
                result = i + 9.01
        for i in dec_part:
            if i.isalpha():
                result = i + 9.01
        result = ''
        int_part = int(int_part)
        if int_part == 0:
            result += '0'
        while int_part != 0:
            result += str(int_part % 2)
            int_part = int_part//2
        result = result[::-1]
        result += '.'
        j = 0
        dec_part = dec_part[::-1]
        dec_part += '.'
        dec_part = dec_part[::-1]
        dec_part = float(dec_part)
        while dec_part != 0:
            if j > 15:
                break
            dec_part = dec_part * 2
            result += str(floor(dec_part))
            dec_part = dec_part - floor(dec_part)
            j += 1
        return result
    else:
        int_part = Decimal
        for i in int_part:
            if i.isalpha():
                result = i + 9.01
        result = ''
        int_part = int(int_part)
        while int_part != 0:
            result += str(int_part % 2)
            int_part = int_part // 2
        result = result[::-1]
        return result


def Decimal_to_Octal(Decimal):
    Decimal_point = Decimal.find('.')
    if Decimal_point >= 0:
        if Decimal_point == 0:
            int_part = '0'
            dec_part = Decimal[Decimal_point + 1:]
        else:
            int_part = Decimal[:Decimal_point]
            dec_part = Decimal[Decimal_point + 1:]
        for i in int_part:
            if i.isalpha():
                result = i + 9.01
        for i in dec_part:
            if i.isalpha():
                result = i + 9.01
        result = ''
        int_part = int(int_part)
        if int_part == 0:
            result += '0'
        while int_part != 0:
            result += str(int_part % 8)
            int_part = int_part//8
        result = result[::-1]
        result += '.'
        j = 0
        dec_part = dec_part[::-1]
        dec_part += '.'
        dec_part = dec_part[::-1]
        dec_part = float(dec_part)
        while dec_part != 0:
            if j > 15:
                break
            dec_part = dec_part * 8
            result += str(floor(dec_part))
            dec_part = dec_part - floor(dec_part)
            j += 1
        return result
    else:
        int_part = Decimal
        for i in int_part:
            if i.isalpha():
                result = i + 9.01
        result = ''
        int_part = int(int_part)
        while int_part != 0:
            result += str(int_part % 8)
            int_part = int_part // 8
        result = result[::-1]
        return result


def Decimal_to_Hexadecimal(Decimal):
    Decimal_point = Decimal.find('.')
    Hexadecimal_Conversions = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    if Decimal_point >= 0:
        if Decimal_point == 0:
            int_part = '0'
            dec_part = Decimal[Decimal_point + 1:]
        else:
            int_part = Decimal[:Decimal_point]
            dec_part = Decimal[Decimal_point + 1:]
        for i in int_part:
            if i.isalpha():
                if i in Hexadecimal_Conversions:
                    continue
                else:
                    result = i + 9.01
        for i in dec_part:
            if i.isalpha():
                if i in Hexadecimal_Conversions:
                    continue
                else:
                    result = i + 9.01
        result = ''
        int_part = int(int_part)
        if int_part == 0:
            result += '0'
        while int_part != 0:
            buffer = int_part % 16
            if buffer in Hexadecimal_Conversions.values():
                for i in Hexadecimal_Conversions.keys():
                    if Hexadecimal_Conversions[i] == buffer:
                        result += i
            else:
                result += str(buffer)
            int_part = int_part//16
        result = result[::-1]
        result += '.'
        j = 0
        dec_part = dec_part[::-1]
        dec_part += '.'
        dec_part = dec_part[::-1]
        dec_part = float(dec_part)
        while dec_part != 0:
            if j > 15:
                break
            dec_part = dec_part * 16
            buffer = floor(dec_part)
            if buffer in Hexadecimal_Conversions.values():
                for i in Hexadecimal_Conversions.keys():
                    if Hexadecimal_Conversions[i] == buffer:
                        result += i
            else:
                result += str(buffer)
            dec_part = dec_part - floor(dec_part)
            dec_part = round(dec_part, 4)
            j += 1
        return result
    else:
        int_part = Decimal
        for i in int_part:
            if i.isalpha():
                if i in Hexadecimal_Conversions:
                    continue
                else:
                    result = i + 9.01
        result = ''
        int_part = int(int_part)
        while int_part != 0:
            buffer = int_part % 16
            if buffer in Hexadecimal_Conversions.values():
                for i in Hexadecimal_Conversions.keys():
                    if Hexadecimal_Conversions[i] == buffer:
                        result += i
            else:
                result += str(buffer)
            int_part = int_part//16
        result = result[::-1]
        return result


def Binary_to_Binary(Binary):
    Binary_to_Octal(Binary)
    return Binary


def Binary_to_Hexadecimal(Binary):
     return Decimal_to_Hexadecimal(str(Binary_to_Decimal(Binary)))


def Binary_to_Octal(Binary):
    return Decimal_to_Octal(str(Binary_to_Decimal(Binary)))


def Hexadecimal_to_Hexadecimal(Hexadecimal):
    Hexadecimal_to_Binary(Hexadecimal)
    return Hexadecimal


def Hexadecimal_to_Binary(Hexadecimal):
    return Decimal_to_Binary(str(Hexadecimal_to_Decimal(Hexadecimal)))


def Hexadecimal_to_Octal(Hexadecimal):
    return Decimal_to_Octal(str(Hexadecimal_to_Decimal(Hexadecimal)))


def Octal_to_Octal(Octal):
    Octal_to_Decimal(Octal)
    return Octal


def Octal_to_Binary(Octal):
    return Decimal_to_Binary(str(Octal_to_Decimal(Octal)))


def Octal_to_Hexadecimal(Octal):
    return Decimal_to_Hexadecimal(str(Octal_to_Decimal(Octal)))


def Decimal_to_Decimal(Decimal):
    for i in Decimal:
        if i.isalpha():
            Decimal += 1
    else:
        return Decimal