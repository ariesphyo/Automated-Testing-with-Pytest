# Task 6 — ဗီဒီယိုတင်ဆက်မှုအတွက် မြန်မာဘာသာ Script

## တင်ဆက်မှု အစီအစဉ်

- **ကြာချိန်:** ၅ မိနစ်မှ ၇ မိနစ်ခန့် (အကြံပြု ၆ မိနစ်)
- **ဗီဒီယိုပုံစံ:** မျက်နှာကို မြင်ရစေပြီး screen ကိုလည်း ပြသပါ။ Terminal command များကို ဖတ်ရလွယ်အောင် ချဲ့ပြပါ။
- **အဓိကရည်ရွယ်ချက်:** Pytest ဖြင့် normal, boundary, invalid input များကို စမ်းသပ်ပုံ၊ fixtures နှင့် parametrization ကို သုံးပုံ၊ coverage နှင့် mutation testing က test suite အရည်အသွေးကို ဘယ်လိုစစ်ပေးသလဲဆိုတာ ရှင်းပြရန်။

အောက်ပါစာသားကို တိုက်ရိုက်ဖတ်နိုင်သလို ကိုယ့်စကားနဲ့လည်း ပြောနိုင်ပါတယ်။ အချိန်အမှတ်များသည် အကြမ်းဖျဉ်းဖြစ်ပြီး command များ အလုပ်လုပ်နေချိန်တွင် ရလဒ်ကို ပြသပြီး ရှင်းပြပါ။

---

## ၁။ မိတ်ဆက် — ၀:၀၀ မှ ၀:၃၅

မင်္ဂလာပါ။ ဒီဗီဒီယိုမှာ Automated Testing with Pytest project ရဲ့ test suite ကို ဘယ်လိုဒီဇိုင်းလုပ်ထားတယ်၊ ဘယ်လို run လုပ်တယ်၊ test quality ကို coverage နဲ့ mutation testing သုံးပြီး ဘယ်လိုစစ်တယ်ဆိုတာ တင်ပြပါမယ်။

ဒီ project မှာ စမ်းသပ်ထားတဲ့ module သုံးခုက calculator functions, user data validator နဲ့ student management system တို့ ဖြစ်ပါတယ်။ အဓိကရည်ရွယ်ချက်က မှန်ကန်တဲ့ input တွေ အလုပ်လုပ်ကြောင်းသာမက boundary နဲ့ invalid input တွေမှာ သတ်မှတ်ထားတဲ့ရလဒ် သို့မဟုတ် exception ကို ပြန်ပေးကြောင်း အတည်ပြုဖို့ ဖြစ်ပါတယ်။

## ၂။ Environment တပ်ဆင်ခြင်းနှင့် အခြေခံအသုံးပြုပုံ — ၀:၃၅ မှ ၁:၂၅

ပထမဦးစွာ repository ရဲ့ root folder ကိုဖွင့်ပြီး Python virtual environment တစ်ခု ဖန်တီးပါမယ်။ Windows PowerShell မှာ အောက်ပါ command တွေကို သုံးနိုင်ပါတယ်။

```powershell
Set-Location "D:\16. Projects\Automated Testing System"
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

`requirements.txt` ထဲမှာ pytest, pytest-cov နဲ့ mutmut ပါဝင်ပါတယ်။ Task 1 အတွက် calculator test များကို run ဖို့ —

```powershell
python -m pytest tests/test_calculator.py -v
```

Task 2 အတွက် data validator test များကို run ဖို့ —

```powershell
python -m pytest tests/test_data_validator.py -v
```

Task 3 အတွက် student manager test များနှင့် fixtures ကို စစ်ဖို့ —

```powershell
python -m pytest tests/test_student_manager.py -v
```

Task 1 မှ 3 အထိ test အားလုံးကို run ဖို့ —

```powershell
python -m pytest tests/ -v
```

Task 4 အတွက် `src/` code coverage ကိုစစ်ပြီး မစမ်းသပ်ရသေးတဲ့ line များကိုကြည့်ဖို့ —

```powershell
python -m pytest tests/ --cov=src --cov-report=term-missing
```

Coverage သည် အနည်းဆုံး 85% ရှိရပါမယ်။ Autograder နှင့် mutant detection scorecard ကို run ဖို့ —

```powershell
python -m pytest autograde_tests/ -v
```

Task 5 ဖြစ်တဲ့ `report.md` ဖြည့်ခြင်းနှင့် Task 6 ဖြစ်တဲ့ video ရိုက်ကူးခြင်းတို့အတွက် terminal command မရှိပါ။ Video တင်ပြီး report ထဲ link ထည့်ကာ စစ်ဆေးမှုများပြီးသွားလျှင် GitHub သို့ တင်သွင်းနိုင်ပါတယ် —

```powershell
git status
git add .
git commit -m "Submit Project 7: Automated Testing with Pytest"
git push origin main
```

## ၃။ Test design — ၁:၂၅ မှ ၃:၁၅

Test design မှာ Equivalence Partitioning နဲ့ Boundary Value Analysis ကို အသုံးပြုထားပါတယ်။ Equivalence Partitioning ဆိုတာ အပြုအမူတူမယ်လို့ မျှော်လင့်ရတဲ့ input တွေကို အုပ်စုခွဲပြီး အုပ်စုတစ်ခုစီက ကိုယ်စားပြုတန်ဖိုးတွေကို စမ်းသပ်တာပါ။ ဥပမာ calculator ရဲ့ score တွေကို valid range, range အပြင်ဘက်နဲ့ numeric မဟုတ်တဲ့ input ဆိုပြီး ခွဲနိုင်ပါတယ်။

Boundary Value Analysis ကတော့ လက်ခံနိုင်တဲ့ အပိုင်းအခြားရဲ့ အစွန်းနဲ့ အစွန်းအနီးက တန်ဖိုးတွေကို အထူးစမ်းသပ်တာပါ။ Calculator မှာ score 0 နဲ့ 100၊ အဲဒီထက်နည်းနည်းလျော့တဲ့ သို့မဟုတ် ကျော်တဲ့တန်ဖိုးတွေကို စမ်းပါတယ်။ Prime စစ်ရာမှာ negative number, 0 နဲ့ 1 ကို false ဖြစ်ကြောင်း၊ 2 နဲ့ 3 က prime ဖြစ်ကြောင်း၊ composite နဲ့ ပိုကြီးတဲ့ prime တွေကိုလည်း စစ်ထားပါတယ်။ Factorial မှာ 0 factorial က 1 ဖြစ်ကြောင်းနဲ့ negative input ကို ပယ်ချကြောင်း စစ်ပါတယ်။

Data validator မှာ မှန်ကန်တဲ့နဲ့ မမှန်ကန်တဲ့ email ပုံစံတွေ၊ password စည်းမျဉ်းတစ်ခုချင်းစီ၊ username ရဲ့ အက္ခရာ ၃ လုံးမှ ၂၀ လုံးအထိ အရှည်၊ အသက် ၁၃ နှစ်မှ ၁၂၀ နှစ်အထိ အပိုင်းအခြားနဲ့ registration မှာ မဖြစ်မနေပါရမယ့် field တွေကို စမ်းသပ်ထားပါတယ်။ Invalid input တွေမှာ သတ်မှတ်ထားတဲ့ exception အမျိုးအစားနဲ့ error message မှန်ကန်ကြောင်းကိုပါ စစ်ထားပါတယ်။

Student management မှာ Student එකක් නිවැරදි දත්ත සමඟ တည်ဆောက်နိုင်မှု၊ grade ကို 0 မှ 100 အတွင်း ထည့်နိုင်မှုနဲ့ GPA conversion အပိုင်းအခြား ငါးခုကို စစ်ပါတယ်။ Manager အတွက် add, retrieve, update, remove စတဲ့ state transitions၊ duplicate ID ပယ်ချမှု၊ ranking နဲ့ minimum GPA အလိုက် filtering ကို စမ်းသပ်ထားပါတယ်။

## ၄။ Pytest Features — ၃:၁၅ မှ ၄:၀၀

တူညီတဲ့စည်းမျဉ်းကို input အများအပြားနဲ့ စမ်းဖို့ `@pytest.mark.parametrize` ကို သုံးထားပါတယ်။ ဒီနည်းက test logic ကို ထပ်မရေးဘဲ normal, boundary နဲ့ invalid case တွေကို တစ်နေရာတည်းမှာ ရှင်းရှင်းလင်းလင်း စမ်းနိုင်စေပါတယ်။

Exception မျှော်လင့်ထားတဲ့အခါ `pytest.raises` နဲ့ exception class ကို စစ်ပြီး၊ လိုအပ်တဲ့နေရာတွေမှာ message ထဲက အကြောင်းရင်းကိုပါ assert လုပ်ထားပါတယ်။ `tests/conftest.py` ထဲက `empty_manager`, `sample_student`, `populated_manager` နဲ့ `valid_registration_data` fixtures တွေက setup ကို ပြန်လည်အသုံးပြုနိုင်စေပြီး test တစ်ခုချင်းစီကို ဖတ်ရလွယ်စေပါတယ်။

## ၅။ Coverage နှင့် Mutation Testing — ၄:၀၀ မှ ၅:၁၅

Coverage က test run လုပ်ချိန်မှာ source code ရဲ့ ဘယ်လောက်ကို execute လုပ်ခဲ့သလဲကို တိုင်းတာတာပါ။ ဒီ project မှာ `pytest-cov` နဲ့ `src/` ရဲ့ statement coverage 100 ရာခိုင်နှုန်း၊ စုစုပေါင်း statement 213 ခုကို အတည်ပြုထားပါတယ်။ ဒါပေမဲ့ coverage မြင့်တာတစ်ခုတည်းနဲ့ test တွေက မှားယွင်းတဲ့အပြုအမူကို ဖမ်းမိတယ်လို့ မဆိုနိုင်ပါဘူး။

အဲဒီအတွက် mutation testing ကို သုံးပါတယ်။ Mutant ဆိုတာ မူရင်း code ထဲမှာ ရည်ရွယ်ချက်ရှိရှိ ထည့်ထားတဲ့ bug အသေးစားတစ်ခုပါ။ ဥပမာ 1 ကို prime လို့ မှားသတ်မှတ်ခြင်း၊ empty average ကို exception မပေးဘဲ ပြန်ပေးခြင်း၊ negative numbers ရဲ့ maximum ကို မှားတွက်ခြင်း၊ invalid email သို့မဟုတ် password ကို လက်ခံခြင်းနဲ့ duplicate student ID ကို overwrite လုပ်ခြင်းတို့ ဖြစ်ပါတယ်။ သက်ဆိုင်ရာ test တွေ fail ဖြစ်ရင် mutant ကို “killed” လို့ခေါ်ပြီး test suite က အဲဒီ bug ကို ဖမ်းမိတယ်လို့ ဆိုနိုင်ပါတယ်။ ဒီ project ရဲ့ ပံ့ပိုးထားတဲ့ mutant evaluator မှာ စမ်းသပ်ထားတဲ့ mutants တွေကို test suite က ဖမ်းမိခဲ့ပါတယ်။

ဒီ project မှာ mutmut ကိုလည်း သတ်မှတ်ထားပါတယ်။ Windows ပေါ်မှာ mutmut ကို တိုက်ရိုက် run လုပ်တာကို လက်ရှိ version က မပံ့ပိုးတဲ့အတွက် Linux သို့မဟုတ် WSL environment ထဲမှာ repository ကိုဖွင့်၊ dependencies တပ်ဆင်ပြီး project root မှာ `mutmut run` ကို သုံးပါ။ WSL ထဲမှာ Python environment သီးခြားရှိတာကြောင့် `python -m pip install -r requirements.txt` ကို WSL မှာပါ run လုပ်ဖို့ လိုပါတယ်။ ဒီနည်းနဲ့ source ကို mutate လုပ်ပြီး configured test suite ကို စမ်းနိုင်ပါတယ်။

```bash
python -m pip install -r requirements.txt
mutmut run
```

## ၆။ AI Engineering နှင့် နိဂုံး — ၅:၁၅ မှ ၆:၀၀

Classical software testing မှာ သတ်မှတ်ထားတဲ့ input နဲ့ expected output ကို နှိုင်းယှဉ်တာများပါတယ်။ AI system တွေမှာတော့ output က အမြဲတမ်း တိတိကျကျ တူညီမနေတဲ့အတွက် benchmark အများအပြားနဲ့ quality ကို တိုင်းတာရပါတယ်။ AI agent/tool-call testing မှာ tool name, argument schema, ခေါ်ဆိုမှုအခြေအနေနဲ့ ရလဒ်ကို စစ်နိုင်ပါတယ်။ LLM-as-a-judge နဲ့ Process Reward Model တွေက အဖြေတင်မက အဆင့်ဆင့်လုပ်ဆောင်မှုကိုပါ အကဲဖြတ်နိုင်ပေမယ့် လူ့ဆုံးဖြတ်ချက်နဲ့ တိုက်ဆိုင်မှု၊ bias နဲ့ consistency ကိုလည်း သတိထားရပါတယ်။

အနှစ်ချုပ်အားဖြင့် test suite က မှန်ကန်တဲ့လုပ်ဆောင်ချက်၊ boundary, invalid input နဲ့ state changes တွေကို စမ်းသပ်ထားပါတယ်။ Parametrization နဲ့ fixtures က စမ်းသပ်မှုတွေကို ထိန်းသိမ်းရလွယ်စေပြီး coverage နဲ့ mutation testing က test suite ရဲ့ အားသာချက်နဲ့ လွတ်နေတဲ့အပိုင်းတွေကို နားလည်စေပါတယ်။ ကြည့်ရှုပေးတဲ့အတွက် ကျေးဇူးတင်ပါတယ်။

---

## အသံသွင်းခြင်းနှင့် တင်သွင်းခြင်း စစ်ဆေးရန်

- တင်ဆက်မှုကို ၅ မိနစ်မှ ၇ မိနစ်အတွင်း ထားပါ။
- ဗီဒီယိုတစ်လျှောက် မျက်နှာကို မြင်ရစေပြီး screen ပေါ်က command နှင့် test result များကို ဖတ်ရှုနိုင်အောင် ပြသပါ။
- `.mp4` အဖြစ် သိမ်းပြီး YouTube, Google Drive သို့မဟုတ် Dropbox တွင် instructor ကြည့်နိုင်သော permission ဖြင့် တင်ပါ။
- ရရှိလာသော share link ကို `report.md` ရှိ **Video Presentation Link** နေရာတွင် ထည့်ပါ။
