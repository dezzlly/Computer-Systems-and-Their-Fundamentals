org 0x100                  ; Начало .COM программы

section .data
    a db 5                 ; Значение a
    b db 10                ; Значение b
    c db 3                 ; Значение c
    resultMsg db 'Result: $'  ; Текст перед числом (для вывода через int 21h)

section .text
_start:
    ; Инициализация сегмента данных (используем CS = DS)
    mov ax, cs
    mov ds, ax

    ; Вычисляем выражение: b - c + a
    mov al, [b]
    sub al, [c]
    add al, [a]
    
    ; Сохраняем результат в AL и готовим для вывода
    ; Разделим результат на десятки и единицы
    mov ah, 0
    mov bl, 10
    div bl              ; AL / 10 → AL = десятки, AH = остаток (единицы)

    ; AL = десятки, AH = единицы

    ; Вывод текста "Result: "
    mov ah, 09h
    lea dx, resultMsg
    int 21h

    ; Печать десятков
    add al, '0'
    mov dl, al
    mov ah, 02h
    int 21h

    ; Печать единиц
    mov al, ah
    add al, '0'
    mov dl, al
    mov ah, 02h
    int 21h

    ; Ожидание нажатия клавиши перед выходом
    mov ah, 0
    int 16h

    ; Завершение программы
    mov ax, 4C00h
    int 21h
