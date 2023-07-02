# Kullanıcıdan alınan bilgiler ile şirket uzantısı ile mail adresi üretme

# Kullanıcı bilgisi alma
User_Name = input("Lütfen adınızı yazınız : ")
# Kullanıcının girdiği bilgilerden boşlukları çıkarma
User_Name = User_Name.replace(" ", "")

User_Surname = input("Lütfen soyadınızı yazınız : ")
User_Surname = User_Surname.replace(" ", "")

Company_Name = input("Lütfen şirketinizin adını yazınız : ")
Company_Name = Company_Name.replace(" ", "")

# Kullanıcıdan alınan bilgilerin birleştirilerek şirkete özel mail adresi oluşturulması
Email_address = User_Name + "." + User_Surname + "@" + Company_Name + ".com"
# Mail adresindeki büyük harflerin küçük harflere çevrilmesi
Email_address = Email_address.lower()

print("Email adresiniz : ", Email_address)