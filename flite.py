import os


## How to use this module ##
# This module required to flite.exe
# Also, put flite.exe in the same directory as this module.
# Write "import flite", You can used this!
# ...But, This module is You need put in the same directory as main.py because doesn't work


## Reference ##
# ["read(content, input_name, input_ext, output_name, output_ext, auto_delete)"]

def read(
        content="", input_name="read_data",
        input_ext="txt",
        output_name="output",
        output_ext="wav",
        auto_delete=False,
        text_mode=False
):
    if not text_mode:
        f = open(f"{input_name}.{input_ext}", "w")
        f.write(content)
        f.write("\n")
        f.close()

    os.system(f'flite --setf int_f0_target_stddev=25 --setf int_f0_target_mean=115 -f {input_name}.{input_ext} -o {output_name}.{output_ext}')

    if auto_delete:
        os.remove(f"{input_name}.{input_ext}")