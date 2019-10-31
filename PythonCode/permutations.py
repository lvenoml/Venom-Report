def permutations(str_in):
    def generate_str(str_out, str_in):
        if len(str_in) == 1:
            list_full.append(str_out+str_in[0])
        else:
            for i_ind in range(len(str_in)):
                str_o = str_out + str_in[i_ind]
                str_i = str_in[:i_ind] + str_in[i_ind+1:]
                generate_str(str_o, str_i)
        return 1
    list_full = []
    generate_str('', str_in)
    list_redu = list(dict.fromkeys(list_full))
    return list_redu

str_input = '1231'
print(permutations(str_input))
