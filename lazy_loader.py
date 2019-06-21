import struct
import pickle

def dump_list_of_strings(list_of_strings, outfpath):
    with open(outfpath, "wb") as  out_handle:
        for elem in list_of_strings:
            l=len(elem)
            b1=struct.pack("<l", l)
            out_handle.write(b1)
            b2=struct.pack("%ds"%l, elem)
            out_handle.write(b2)


def read_list_of_strings(infpath):
    with open(infpath, "rb") as  in_handle:
        while True:
            b1=in_handle.read(4)
            if not b1:
                break   # end of file reached
            l=struct.unpack("<l", b1)
            l=l[0]   # should be a long
            b2=in_handle.read(l)    
            elem=struct.unpack("%ds"%l, b2)
            yield elem[0]


def dump_objs(list_of_objs, outfpath):
    strs=[pickle.dumps(x) for x in list_of_objs]
    dump_list_of_strings(strs, outfpath)

    
    
def load_objs(infpath):
    strs=read_list_of_strings(infpath)
    for s in strs:
    	yield pickle.loads(s)



