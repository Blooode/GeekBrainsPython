# � ��������� ����� ������ ������� ��� ����� �������������� ������ � ����������� �������� ��� ��� ������ �������.
# �� ������ ������ ����� ������ ��� ��������. �������� ���������� �������� � ������ �� ��� �������.
# �������� ���������� ����� ����, ������� ����� ���������� ��� ���.

pupils_class1 = int(input("Enter the amount of pupils in first class: "))
pupils_class2 = int(input("Enter the amount of pupils in second class: "))
pupils_class3 = int(input("Enter the amount of pupils in third class: "))
pupils_all = pupils_class1 + pupils_class2 + pupils_class3
if pupils_all % 2 == 0:
    table_amount = pupils_all / 2
else:
    table_amount = pupils_all // 2 + 1
print(f"Amount of tables is {int(table_amount)}")
