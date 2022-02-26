c$ = 0
tv64 = 4
d$ = 8
a$ = 32
b$ = 40
int mystery(int,int) PROC                              ; mystery
$LN3:
        mov     DWORD PTR [rsp+16], edx ; save b at [rsp+16]
        mov     DWORD PTR [rsp+8], ecx  ; save a at [rsp+8]
        sub     rsp, 24
        mov     eax, DWORD PTR a$[rsp]  ; a$[rsp] syntax is same as [rsp+a$]
        mov     ecx, DWORD PTR b$[rsp]
        sub     ecx, eax                ; b - a
        mov     eax, ecx
        mov     DWORD PTR tv64[rsp], eax ; save b - a result at [rsp+tv64]
        mov     eax, DWORD PTR a$[rsp]
        cdq                             ; extended eax value to edx for signed division
        idiv    DWORD PTR b$[rsp]       ; Not sure but modulo
        mov     eax, edx
        mov     ecx, DWORD PTR tv64[rsp]
        imul    ecx, eax                ; c = (b - a) * (a % b)
        mov     eax, ecx
        mov     DWORD PTR c$[rsp], eax  
        mov     eax, DWORD PTR a$[rsp]
        imul    eax, DWORD PTR b$[rsp]  ; c * a
        mov     ecx, DWORD PTR c$[rsp]
        add     ecx, eax                ; (c * a) + b
        mov     eax, ecx
        mov     DWORD PTR d$[rsp], eax  ; d = (c * a) + b
        imul    eax, DWORD PTR b$[rsp], 5 ; b * 5
        mov     ecx, DWORD PTR a$[rsp]
        imul    ecx, DWORD PTR c$[rsp]  ; a * c
        add     eax, ecx                ; b * 5 + a * c
        mov     ecx, DWORD PTR b$[rsp]
        imul    ecx, DWORD PTR d$[rsp]  ; b * d
        sub     eax, ecx                ; b * 5 + a * c - b * d
        add     rsp, 24
        ret     0
int mystery(int,int) ENDP                              ; mystery
