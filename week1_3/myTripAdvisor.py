from bs4 import BeautifulSoup
import requests

data = []
url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'

webdata = requests.get(url)
# print(webdata.text)
soup = BeautifulSoup(webdata.text, 'lxml')
# print(soup)
# titles = soup.select('.top_attractions > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > div > div:nth-of-type(1) > a.poiTitle')#[target="_blank"]')
titles = soup.select('a.poiTitle')#[target="_blank"]')
# images = soup.select('.top_attractions > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > a:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) > img:nth-of-type(1)')
images = soup.select('img[width="200"]')# set image width can eliminate other images we dont need
cates = soup.select('div.detail > div:nth-of-type(3)')# > div:nth-of-type(1)')# > div:nth-of-type(1) > div:nth-of-type(2) > div')
# print(titles)
# print(images)
# print(cates)
# for title in titles:
#     print(title.get_text())
# for image in images:
#     print(image.get('src'))
# for cate in cates:
#     print(cate.get_text())
# for title, image, cate in zip(titles, images, cates):
#     info = {
#         "title:" : title.get_text(),
#         "image:" : image.get('src'),
#         "cate:" : cate.get_text(),
#     }
#     data.append(info)
#
# for d in data:
#     print(d)
# url_save = 'https://cn.tripadvisor.com/Saves/37685322'
url_save = 'https://cn.tripadvisor.com/Saves/63376875'
headers = {
  'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0',
  'Cookie' : 'TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_162*RS.1; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Ccatchsess%2C3%2C-1%7Cbrandsess%2C%2C-1%7CCpmPopunder_1%2C%2C-1%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7Cmultipers%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1497681135%7CLaFourchette+MC+Banners%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C104-771-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7Cmultisess%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CCPNC%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAUD=LA-1497072126125-1*RDD-1-2017_06_10*LG-88082280-2.1.F.*LD-88082281-.....; TASSK=enc%3AAFB82URPBHCWbH0B40jgWHaujIlacImsHiL8vVzimeIRCRLrch%2BEAWjafYkg1XFcpGNtNXPczmAU7u8nKCH888HsM%2BPgv%2F2MSlM4Zn5rtcXzAFqL8vTqwH3PnrEov5VgPQ%3D%3D; PAC=AGB6U78GL0DTrDIhyJXsdtsQ1_7UFL0TTF10kuCACEadHaA9XKH_8FWHGHAlTXddB9B226dX2WULRZ88jUFDqIbxaJjm1-l2tNcTtcmdBo0fgJXo53gN-VOi4AK3FAc2bOSMh1985FR2MdrI8_xfcdlLDJcOTxT0C6LwpHQRYVTzTE7sWEB3F-duB72eu4OlddvbgQc8LQET8DkOoBl-0uo%3D; PMC=V2*MS.40*MD.20170610*LD.20170611; TAUnique=%1%enc%3AidzSKa%2BDPH3d4ouJUwL9EXqEy6o2d7JkTAhU%2FyeluYNirck%2BOLs3gg%3D%3D; TART=%1%enc%3A3eKLiVMC%2FREJiq4U0pNTN7IbfPyQnRpsWAv9HSpkOleL253GyFyjk00uBRozvvmDQdi%2FcfE8Vg4%3D; __gads=ID=f6daefb98f909ca0:T=1497072129:S=ALNI_MbIElTVH6uehpUp_Dj4u63pmWzp0w; TASession=%1%V2ID.983F15CE3F36470B5634B4A8ED59B0A0*SQ.63*PR.39776%7C*LS.RegistrationController*GR.24*TCPAR.89*TBR.12*EXEX.51*ABTR.16*PHTB.12*FS.61*CPU.37*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.02201B0F109B826CD2216941827FC597*FA.1*DF.0*FLO.60763*TRA.true*LD.60763; ServerPool=A; TAReturnTo=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; roybatty=TNI1625!AMJL57R5LDnxPkosVwlw0CPfDl0MuGyHlMGRtrXmkf%2BZ3CoXOwJB8lvL9hEgbduUs0t%2BZoDSqNutz5LbJgkU1K%2B6pByLAaHFxrlsHPNBNXmjn5V7ToGqkdYtEwGtyp9oGqM1j%2FzUzrsYNpQFwfUZQzkltzYfEqJLIGqP0A%2Bthx%2B3%2C1; SecureLogin2=3.4%3AAKqF0cjFnePPOFAJUoCrCvakWWDjHAc6KSGBLRMq37Q467JZWVooY%2BFFfvizywMiZ%2Bk6AO6ye2H5GOGWmO4mo%2BrbJuEeRRK3bMeNkOoAYG3Dr6zq8i%2BnUaafwHsbaUvRlwbcsRfmmUzPuA2dQCCPDLLy%2BnV6cvI7p%2FYx3X4KjJ4Xv1wBDz461cha3bwT%2FEhIlL43nwLEH9qW7bEvL6agV7I%3D; TAAuth3=3%3A8acdef3aa7b80727edabf1ff1ad2c197%3AAO7ST9J03RGIstbgkn8mk86MNFNyeJ3aJV%2FAPTJx3twoaU2cpWrvAg8b70Kf6VgSbW0u61kL7UyMPBbrT4b1yOquMp7ve8QAJdKmMrxku9XJ2PjZE46CZ5yXTvpjP70WtdOIUY1b28eHWzQuGt84hI%2BIaAvx9904yCeVrHZOL%2BnrXVInIt7Aa7K5A8rgKEYMJQ%3D%3D',
}

web_save_data = requests.get(url_save, headers = headers)
soup = BeautifulSoup(web_save_data.text, 'lxml')
print(soup)
