ROP_DEST = 0x1464F300 - 0x4
ROP_OFFSET_KSN = 0xEF1AC

ADD_R0R0R4_POP_R4PC = 0x250290

CMP_R0R1_MOVGT_R0_1_MOVLE_R0_0_POP_R4PC = 0x21d644

DSP_REGISTERINTERRUPTEVENTS = 0x11db70
DSP_UNLOADCOMPONENT = 0x11dadc
DSP_HANDLE = 0x3D2B94

FS_CLOSEFILE = 0x26a2a4
FS_MOUNTSDMC = 0x26aaf8
FS_TRYGETSIZE = 0x26a1b8
FS_TRYOPENFILE = 0x26a210
FS_TRYREADFILE = 0x10e53c
FSUSER_HANDLE = 0x3D2C28

GSPGPU_FLUSHDATACACHE = 0x12b6d8
GSPGPU_FLUSHDATACACHE_WRAPPER = 0x1266cc
GSPGPU_GXCMD4 = 0x1267cc
GSPGPU_GXTRYENQUEUE = 0x250728
GSPGPU_GXTRYENQUEUE_WRAPPER = 0x1265DC
GSPGPU_INTERRUPT_RECEIVER_STRUCT = 0x3C0C40
GSPGPU_HANDLE = 0x3E477C

LDR_R0R0_POP_R4PC = 0x12e8d4
LDR_R0R0_STR_R0R1_POP_R4PC = 0x115cb8
LMSI_MEMCMP = 0x12f3c0

MOV_SP_R0_MOV_R0R2_MOV_LRR3_BX_R1 = 0x14356c

NOP = 0x100b4c

POP_R0PC = 0x249244
POP_R0R1R2R3R4PC = 0x159358
POP_R11PC = 0x124a1c
POP_R1PC = 0x252618
POP_R1R2R3R4R5PC = 0x3395d4
POP_R1R2R3R4R5R6R7PC = 0x15bf54
POP_R3PC = 0x103c8c
POP_R3R4R5R6R7R8R9PC = 0x1046e8
POP_R4LR_BX_R1 = 0x1021c0
POP_R4PC = 0x100270
POP_R4R5PC = 0x100ac0
POP_R4R5R6R7R8R9R10R11PC = 0x101710
POP_R4R5R6R7R8R9R10R11R12PC = 0x11a310
POP_R4R6PC = 0x2976d4

STRB_R0R4_POP_R4PC = 0x100ce0
STREQ_R0R4_2C_POP_R4PC = 0x26394c
STR_R0R1_POP_R4PC = 0x115cbc
SUB_SPSPR3_MOV_R1SP_STR_R3SP_MIN4INC_BLX_R2 = 0x13e5b4

SVC_EXITTHREAD = 0x11bb94
SVC_SLEEPTHREAD = 0x25e71c

MAIN_THREAD_BREAK = 0x154D9D00 + 0x8
MAIN_THREAD_POP_PTR = 0x0FFFFCE4

THREAD1_BREAK = 0x3C0C40 + 0x77
