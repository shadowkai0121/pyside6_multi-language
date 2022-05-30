# pyside6_multi-language
PySide6 動態多語系切換範本

### 建立字典檔流程

1.  使用 lfupdate 產生字典檔
    
    ```bash
    pyside6-lupdate.exe ui_main.ui -ts ui_main_us.ts
    pyside6-lupdate.exe ui_main.ui -ts ui_main_tw.ts
    ```
    
2. 使用 linguist 編輯字典內容
    
    ```bash
    pyside6-linguist ui_main_tw.ts
    pyside6-linguist ui_main_us.ts
    ```
    
3. 在 linguist 內使用釋出或者使用 pyside6-lrease 指令產生 qm 檔
