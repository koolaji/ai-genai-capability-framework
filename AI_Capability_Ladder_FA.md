# نردبان ۱۰ سطحی توانمندی AI / GenAI — مبنای کتاب‌محور

_ساختار سطوح بر پایهٔ ادبیات شناخته‌شدهٔ کسب مهارت، شناخت و بلوغ فرایند بنا شده است؛ نه مدل‌های بازاریابی فروشندگان._

## ستون فقرات علمی نردبان

| منبع (کتاب) | نقش در نردبان |
|---|---|
| **Dreyfus & Dreyfus, _Mind Over Machine_ (1986)** | پنج مرحلهٔ کسب مهارت: Novice → Advanced Beginner → Competent → Proficient → Expert |
| **Patricia Benner, _From Novice to Expert_ (1984)** | کاربست همان پنج مرحله در عمل حرفه‌ای و سازمانی |
| **Bloom (1956) / Anderson & Krathwohl (2001)** | عمق شناختی هر سطح: Remember → Understand → Apply → Analyze → Evaluate → Create |
| **Watts Humphrey, _Managing the Software Process_ (1989)** (ریشهٔ CMM/CMMI) | بلوغ فرایند: Initial → Managed → Defined → Quantitatively Managed → Optimizing |
| **Forsgren, Humble, Kim, _Accelerate_ (2018)** | مدل قابلیت و سنجش تحویل (DORA) برای سطوح کاری |
| **Beyer et al., _Site Reliability Engineering_ (2016)** | toil، automation و error budget برای سطوح اتوماسیون |
| **Skelton & Pais, _Team Topologies_ (2019)** | پلتفرم به‌مثابه سرویس، برای سطح ۹ |
| **Russell & Norvig, _AI: A Modern Approach_ (4th ed.)** | مبانی agent و یادگیری برای سطوح ساخت |
| **Stuart Russell, _Human Compatible_ (2019)** · **Brian Christian, _The Alignment Problem_ (2020)** · **Cathy O'Neil, _Weapons of Math Destruction_ (2016)** | نظارت انسانی، هم‌راستایی و ریسک مدل/سوگیری |
| **Agrawal, Gans, Goldfarb, _Prediction Machines_ (2018)** | اقتصاد پذیرش و ROI برای سطوح راهبری |
| **Spencer & Spencer, _Competence at Work_ (1993)** | روش مدل‌سازی شایستگی برای روبریک HR |

> استانداردها (NIST AI RMF، ISO/IEC 42001، OWASP LLM Top 10، SR 11-7) فقط به‌عنوان **مرجع کنترل** به‌کار رفته‌اند، نه مبنای سطوح.

---

## L1 — بدون مواجهه (پیش از Novice)
**مبنا:** Dreyfus: پیش‌از‌Novice · Bloom: پیش‌از‌Remember · CMMI: Initial (موردی/کنترل‌نشده) · کتاب: Humphrey (1989), Benner (1984) فصل ۱.
**خلاصه:** از ابزار GenAI مجاز استفاده نکرده؛ مدل ذهنی از توان/خطر آن ندارد.
**رفتار:** در کار از AI استفاده نمی‌کند؛ قواعد پایه را نمی‌داند.
**ایمنی/حاکمیت:** ریسک اصلی = paste دادهٔ محرمانه در ابزار عمومی (O'Neil 2016؛ Russell 2019).
**شواهد برای HR:** هیچ (وضعیت آغازین).
**آموزش برای L2:** «سواد AI سازمانی ۱۰۱» (هم‌راستا با Remember در Bloom و الزام سواد EU AI Act).
**پرچم قرمز:** استفاده از ابزار مصرفی غیرمجاز «فقط برای امتحان».

## L2 — آگاهی (آغاز Novice)
**مبنا:** Dreyfus: Novice (پیروی از قواعد بی‌توجه به زمینه) · Bloom: Remember · CMMI: Initial→ · کتاب: Dreyfus & Dreyfus (1986).
**خلاصه:** می‌داند GenAI چه می‌کند/نمی‌کند، ابزار مجاز را می‌شناسد و **قواعد طبقه‌بندی داده را پیش از هر استفاده** می‌داند.
**رفتار:** GenAI را به زبان ساده توضیح می‌دهد؛ hallucination را به‌عنوان حالت شکست می‌شناسد؛ می‌داند کدام ابزار برای کدام کلاس داده مجاز است.
**ایمنی/حاکمیت:** قواعد عمومی/داخلی/محرمانه/محدود را می‌داند؛ دادهٔ محدود هرگز بدون تأیید به مدل داده نمی‌شود.
**شواهد برای HR:** قبولی ارزیابی اجباری سواد AI + پذیرش acceptable-use.
**آموزش برای L3:** آشنایی عملی با ابزار چت مجاز؛ مبانی prompt ایمن.
**پرچم قرمز:** باور به اینکه خروجی AI مرجع قطعی است.

## L3 — کاربر پایه (Advanced Beginner)
**مبنا:** Dreyfus: Advanced Beginner (تشخیص جنبه‌های موقعیتی با راهنمایی) · Bloom: Understand + Apply (پایه) · CMMI: Managed (پایه) · کتاب: Benner (1984), Bloom/Anderson.
**خلاصه:** از GenAI مجاز برای کارهای روزمرهٔ کم‌ریسک استفاده می‌کند و **راستی‌آزمایی** و قواعد داده را قابل‌اتکا رعایت می‌کند.
**رفتار:** پیش‌نویس/خلاصه/بازنویسی با AI؛ همیشه پیش از استفاده بازبینی می‌کند؛ دادهٔ حساس را ماسک می‌کند.
**ایمنی/حاکمیت:** هر خروجی را راستی‌آزمایی می‌کند؛ AI را «پیش‌نویس» می‌داند نه «منبع».
**شواهد برای HR:** گواهی مدیر بر استفادهٔ ایمن روزمره + نمونهٔ کار بازبینی‌شده.
**آموزش برای L4:** مهندسی prompt ساختاریافته (few-shot، تجزیهٔ مسئله، قالب خروجی).
**پرچم قرمز:** کپی‌وپیست عینی خروجی AI در محصول قابل‌تحویل.

## L4 — کاربر اثربخش prompt (Advanced Beginner → Competent)
**مبنا:** Dreyfus: گذار به Competent · Bloom: Apply · CMMI: Managed · کتاب: Bloom/Anderson, Dreyfus & Dreyfus.
**خلاصه:** با فنون سنجیدهٔ prompt به نتایج قابل‌اتکا می‌رسد و می‌داند کِی AI ابزار مناسبی نیست.
**رفتار:** prompt را روشمند بازنگری می‌کند؛ few-shot/chain-of-thought/خروجی ساختاریافته؛ الگوی hallucination را تشخیص و اصلاح می‌کند.
**ایمنی/حاکمیت:** prompt را طوری می‌سازد که منبع/عدم‌قطعیت بخواهد؛ استناد ساختگی را رد می‌کند؛ از prompt injection آگاه است (OWASP LLM #1).
**شواهد برای HR:** پورتفوی prompt (قبل/بعد) + تله‌متری پذیرش با بازکاری کم.
**آموزش برای L5:** یکپارچه‌سازی AI در جریان‌های چندمرحله‌ای؛ اسکریپت‌نویسی سبک.
**پرچم قرمز:** پذیرش استناد ساختگی؛ نادیده‌گرفتن نشانهٔ عدم‌قطعیت.

## L5 — کاربر جریان کاری (Competent)
**مبنا:** Dreyfus: Competent (برنامه‌ریزی آگاهانه، انتخاب هدف) · Bloom: Apply + Analyze · CMMI: Defined · کتاب: **Accelerate (2018)** (مدل قابلیت/DORA).
**خلاصه:** AI را در یک جریان چندمرحله‌ای می‌گنجاند و نتیجه را **اندازه‌گیری** می‌کند.
**رفتار:** AI را در مراحل زنجیر می‌کند (research→draft→review→format)؛ prompt را برای فرایندِ تکرارشونده استاندارد می‌کند؛ زمان/کیفیت را رصد می‌کند.
**ایمنی/حاکمیت:** نقاط بازبینی انسانی را در جریان تعبیه می‌کند؛ مستند می‌کند کدام مراحل با AI انجام شده‌اند (قابلیت حسابرسی).
**شواهد برای HR:** جریان مستند + metric پیش/بعد (DORA: lead time، change-failure).
**آموزش برای L6:** اشتراک/استانداردسازی الگو برای دیگران؛ مربی‌گری.
**پرچم قرمز:** بهینه‌سازی سرعت فردی همراه با افزایش دوباره‌کاری پایین‌دستی (هشدار پایداری _Accelerate_).

## L6 — کاربر حرفه‌ای (Competent → Proficient)
**مبنا:** Dreyfus: گذار به Proficient (درک کل‌نگر موقعیت) · Bloom: Analyze · CMMI: Defined · کتاب: _Accelerate_, _Site Reliability Engineering_ (فرهنگ اشتراک).
**خلاصه:** متخصص شناخته‌شدهٔ AI تیم که استفادهٔ مؤثر همگان را بالا می‌برد و هنجار ایمن محلی را تعریف می‌کند.
**رفتار:** منتورینگ، گردآوری کتابخانهٔ prompt، تعریف قرارداد AI تیم، ارزیابی ابزار جدید.
**ایمنی/حاکمیت:** مالک هنجار استفادهٔ ایمن تیم؛ مرجع اول «آیا این مجاز است؟»؛ ارجاع به حاکمیت.
**شواهد برای HR:** محصول تیمی پذیرفته‌شده (کتابخانهٔ prompt/قرارداد) + بهبود metric تیم + سابقهٔ منتورینگ.
**آموزش برای L7:** یکپارچه‌سازی برنامه‌محور AI (API، eval harness، مبانی RAG/MLOps).
**پرچم قرمز:** تبلیغ ابزار بدون اندازه‌گیری؛ ترویج میان‌بُرهای دادهٔ غیررسمی.

## L7 — مشارکت‌کنندهٔ اتوماسیون (Proficient)
**مبنا:** Dreyfus: Proficient · Bloom: Analyze + Evaluate · CMMI: Quantitatively Managed · کتاب: **_Site Reliability Engineering_ (2016)** (automation/toil/error budget)، Russell & Norvig (tool use).
**خلاصه:** اتوماسیون‌های مبتنی بر AI را در production با API و **کنترل صریح تأیید/بازگشت** می‌سازد.
**رفتار:** کد می‌نویسد که مدل/ابزار را برای کار واقعی صدا می‌زند؛ مدیریت خطا، logging، idempotency؛ انتشار پشت review gate.
**ایمنی/حاکمیت:** **human-in-the-loop برای write/delete، rollback آزمون‌شده**، least-privilege، audit logging؛ اقدامات کاهشی OWASP LLM.
**شواهد برای HR:** اتوماسیون مستقر + logs + نتیجهٔ eval + دروازهٔ تأیید مستند.
**آموزش برای L8:** طراحی سیستم/راه‌حل؛ معماری بازیابی؛ چارچوب eval.
**پرچم قرمز:** اجرای خودکار write/delete بدون تأیید؛ اتوماسیون «نمایشی» در production.

## L8 — طراح راهکار (Proficient → Expert)
**مبنا:** Dreyfus: گذار به Expert · Bloom: Evaluate · CMMI: Quantitatively Managed · کتاب: Russell & Norvig، **Russell _Human Compatible_ (2019)**، **Christian _The Alignment Problem_ (2020)**.
**خلاصه:** راهکار سرتاسری AI را برای یک مسئلهٔ کسب‌وکار طراحی می‌کند و ارزش آن را با eval اثبات می‌کند.
**رفتار:** انتخاب build/buy و RAG/fine-tune/prompt؛ تعریف eval و SLA؛ طراحی سطح کنترل؛ توجیه موازنهٔ هزینه/تأخیر/ریسک.
**ایمنی/حاکمیت:** **NIST AI RMF** را در طراحی می‌گنجاند؛ Responsible-AI assessment و model factsheet تولید می‌کند؛ از **SR 11-7** عبور می‌کند (مستندسازی، اعتبارسنجی مستقل، fallback).
**شواهد برای HR:** راهکار تحویل‌شده + سند معماری + نتیجهٔ eval + بازنگری موفق ریسک مدل.
**آموزش برای L9:** مهندسی پلتفرم/چارچوب agent؛ ارکستراسیون چندعاملی.
**پرچم قرمز:** افزودن کنترل به‌صورت الصاقی پس از طراحی؛ نبود راهبرد اندازه‌گیری.

## L9 — سازندهٔ پلتفرم/Agent (Expert)
**مبنا:** Dreyfus: Expert (شهود مبتنی بر تجربهٔ عمیق) · Bloom: Create · CMMI: Optimizing · کتاب: **_Team Topologies_ (2019)** (پلتفرم به‌مثابه سرویس)، Russell & Norvig.
**خلاصه:** چارچوب‌های agentic و پلتفرم‌های مشترک AI را می‌سازد که تیم‌های دیگر رویش کار می‌کنند، با ایمنی/حاکمیت تعبیه‌شده.
**رفتار:** ارکستراسیون چندعاملی، لایهٔ guardrail، چارچوب eval، golden datasets در سطح سازمان.
**ایمنی/حاکمیت:** **کنترل‌های ISO/IEC 42001** به‌عنوان قابلیت پلتفرم؛ model inventory، kill-switch، audit، sanctioned-gateway، سه خط دفاع.
**شواهد برای HR:** پلتفرم/چارچوب مورد استفادهٔ چند تیم + guardrail مستند + تأییدیهٔ حاکمیتی.
**آموزش برای L10:** استراتژی سازمانی، سیاست‌گذاری، تعامل مقرراتی، نفوذ اجرایی.
**پرچم قرمز:** خودمختاری بدون kill-switch؛ پلتفرمی که اجازهٔ دور زدن کنترل را می‌دهد.

## L10 — رهبر استراتژی و حاکمیت (Expert راهبردی)
**مبنا:** Dreyfus: Expert (در سطح سازمان) · Bloom: Create · CMMI: Optimizing · کتاب: **_Prediction Machines_ (2018)** (اقتصاد پذیرش)، Russell _Human Compatible_ (حاکمیت).
**خلاصه:** استراتژی سازمانی AI را تعیین و چارچوب حاکمیت/ریسک/سیاست را که گسترش ایمن AI را ممکن می‌کند در اختیار دارد.
**رفتار:** تعریف استراتژی و سرمایه‌گذاری؛ ریاست/مشاورهٔ شورای بازنگری AI؛ مالک مسیر بلوغ حاکمیتی؛ توازن نوآوری و ریسک.
**ایمنی/حاکمیت:** مالک کل چارچوب: **NIST AI RMF، ISO/IEC 42001، SR 11-7، سه خط دفاع، تعامل با ناظر، model inventory، پاسخ به incident**.
**شواهد برای HR:** استراتژی و چارچوب حاکمیت تصویب‌شده + نتایج ممیزی/نظارتی + سابقهٔ رهبری شورا.
**آموزش:** سقف نردبان؛ رشد بیشتر = گسترهٔ اختیارات و نفوذ بر هیئت‌مدیره/ناظر.
**پرچم قرمز:** استراتژی‌ای که اجازه می‌دهد قابلیت‌ها از کنترل‌ها جلو بزنند؛ حاکمیت کاغذی.

---

## نگاشت سریع: سطح ↔ کتاب

| سطح | Dreyfus | Bloom | CMMI |
|---|---|---|---|
| L1 | پیش‌از‌Novice | — | Initial |
| L2 | Novice | Remember | Initial→ |
| L3 | Advanced Beginner | Understand/Apply | Managed |
| L4 | →Competent | Apply | Managed |
| L5 | Competent | Apply/Analyze | Defined |
| L6 | →Proficient | Analyze | Defined |
| L7 | Proficient | Analyze/Evaluate | Quantitatively Managed |
| L8 | →Expert | Evaluate | Quantitatively Managed |
| L9 | Expert | Create | Optimizing |
| L10 | Expert (راهبردی) | Create | Optimizing |

---

## منابع (کتاب‌ها)
- Dreyfus, H. L., & Dreyfus, S. E. (1986). _Mind Over Machine_. Free Press.
- Benner, P. (1984). _From Novice to Expert_. Addison-Wesley.
- Bloom, B. S. (1956). _Taxonomy of Educational Objectives_. / Anderson, L. W., & Krathwohl, D. R. (2001). _A Taxonomy for Learning, Teaching, and Assessing_.
- Humphrey, W. S. (1989). _Managing the Software Process_. Addison-Wesley.
- Forsgren, N., Humble, J., & Kim, G. (2018). _Accelerate_. IT Revolution.
- Beyer, B., Jones, C., Petoff, J., & Murphy, N. R. (2016). _Site Reliability Engineering_. O'Reilly.
- Skelton, M., & Pais, M. (2019). _Team Topologies_. IT Revolution.
- Russell, S., & Norvig, P. _Artificial Intelligence: A Modern Approach_ (4th ed.). Pearson.
- Russell, S. (2019). _Human Compatible_. Viking.
- Christian, B. (2020). _The Alignment Problem_. Norton.
- O'Neil, C. (2016). _Weapons of Math Destruction_. Crown.
- Agrawal, A., Gans, J., & Goldfarb, A. (2018). _Prediction Machines_. HBR Press.
- Spencer, L. M., & Spencer, S. M. (1993). _Competence at Work_. Wiley.
