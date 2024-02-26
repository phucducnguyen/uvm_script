#!/usr/bin/python

import os

directory_name ="bob"

boxes={}
cur_box=None

class BOX:
    def __init__(self,type_name,name):
        self.name=name
        self.type=type_name
        self.dir=directory_name
        self.contains=[]
        self.sends=[[]]
    
class CONTAIN:
    def __init__(self, class_name, var_name) -> None:
        self.class_name=class_name
        self.var_name=var_name

class MSG:
    def __init__(self,mname,mdata_type) -> None:
        self.mname=mname
        self.mdata_type=mdata_type
        
class SEND:
    def __init__(self,msg,vname):
        self.msg=msg
        self.vname=vname
        

def do_dir(toks):
    global directory_name
    directory_name=toks[1]

def do_sb(toks):
    global boxes
    global cur_box
    b=BOX(toks[0],toks[1])
    if toks[1] in boxes:
        print("Hey, you already made a box", toks[1])
        return
    boxes[toks[1]] = b
    cur_box=b
        
def do_contains(toks):
    global cur_box
    c=CONTAIN(toks[1],toks[2])
    cur_box.contains.append(c)

def do_msg(toks):
    global msgs
    m=MSG(toks[1], " ".join(toks[2:]))
    msgs[toks[1]]=m    

def do_send(toks):
    global cur_box
    s=SEND(toks[1],toks[2])
    cur_box.sends.append(s)
    
action_map={
    "directory":do_dir,
    "scoreboard":do_sb,
    "contains":do_contains,
    "env":do_sb,
    "monitor":do_sb,
    "message":do_msg,
    "send":do_send
}

def readit(fn):
    with open(fn,"r") as f:
        for line in f:
            line = line.strip()
            if len(line)<1:
                continue
            if line[0]=='#':
                continue
            toks=line.split()
            if toks[0] in action_map:
                action_map[toks[0]](toks)
            else:
                print("Sorry, I dont understand {toks[0]}\n")

def w_new(b,fo):
    fo.write(f"""  function new(string name=\"{b.name}\",uvm_component par=null);
                 super.new(name,par);
            endfunction : new
             """)
    
def w_contain_vars(b,fo):
    if len(b.contains) ==0:
        return
    for c in b.contains:
        fo.write(f"  {c.class_name} {c.var_name};\n")

def w_send_vars(b,fo):
    if len(b.send)==0:
        return
    for s in b.sends:
        fo.write(f"  uvm_tlm_analysis_port #{msgs[s.msg].mdata_type} {s.vname};\n")
        
def w_build(b,fo):
    if len(b.contains)==0:
        return
    fo.write(f"  function void build_phase(uvm_phase phase);\n")
    for c in b.contains:
        fo.write(f"    {c.var_name}={c.class_name}type_id::create(\"{c.var_name}\",this)\n")
    fo.write(f"  endfunction : build_phase\n")

# def w_connect(b,fo)
def w_run(b,fo):
    fo.write(f"""
  task run_phase(uvm_phase phase);
  // ========== start of {b.name} run phase code ==========
  
  // ========== end of run phase code ==========
  endtask : run_phase             
""")

def emit_box(b):
    if not os.path.exists(b.dir):
        os.makedirs(b.dir)
    p=b.dir+"/"+b.name+".svh"
    with open(p,"w") as fo:
        fo.write(f"//magically created file {p}\n")
        fo.write(f"class {b.name} extends uvm_{b.type};\n")
        fo.write(f"  `uvm_component_utils({b.name})\n")
        w_contain_vars(b,fo)
        w_send_vars(b,f)
        w_new(b,fo)
        w_build(b,fo)
        # w_connect(b,fo)
        w_run(b,fo)
        
        fo.write(f"endclass : {b.name}\n")

def emit_boxes():
    global boxes
    for b in boxes:
        emit_box(b)
        
readit("tc1.txt")
emit_boxes()
# print(directory_name)
# print()