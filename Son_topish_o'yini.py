from random import randint

print("Assalomu alaykum \n\"Son topish\"o'yiniga xush kelibsiz!")

KOMPYUTER_TANLAGAN_SON = randint(1, 1000)
URINISHLAR_SONI = 9

for i in range(URINISHLAR_SONI, -1, -1):
    ODAM_TANLAGAN_SON = int(input("\nSon kiriting: "))
    if ODAM_TANLAGAN_SON < 1 and ODAM_TANLAGAN_SON > 1000:
        print("Mavjud bo'lmagan son")
    elif ODAM_TANLAGAN_SON < KOMPYUTER_TANLAGAN_SON:
        print("\nSiz tanlagan son, kompyuter tanlagan sondan kichkina")
    elif ODAM_TANLAGAN_SON > KOMPYUTER_TANLAGAN_SON:
        print("\nSiz tanlagan son, kompyuter tanlagan sondan katta")
    elif ODAM_TANLAGAN_SON == KOMPYUTER_TANLAGAN_SON:
        print("\nTabriklayman, siz yutdingiz🐉")

    print(f"\nSizda {i}ta urinishlar qo'ldi")
print(f"Kompyuter tanlagan son {KOMPYUTER_TANLAGAN_SON} edi")