from myfunc import add

def main():
    print("=== โปรแกรมคำนวณผลรวมของ A + B ===")
    
    # รับค่าจากผู้ใช้
    a = float(input("ป้อนค่าของ A: "))
    b = float(input("ป้อนค่าของ B: "))

    # เรียกใช้ฟังก์ชัน add จาก myfunc.py
    result = add(a, b)

    # แสดงผลลัพธ์
    print(f"ผลลัพธ์ของ A + B คือ: {result}")

if __name__ == "__main__":
    main()