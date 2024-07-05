# PGCHelper

The PGC Helper is a web automation tool for triggering the randomizer button on the [PGC Memebers Mint Page](https://pgc-members.xyz). 

PGCHelper uses the Selenium library and is written in Python3. 

## How Script Works
* Check command-line arguments
    - If args ok:
        + Start session
            * Go to target site
            * Find target element
            * Trigger element
            * Delay
            * Repeat
    - Args not ok:
        + Do not start session

## Requirements
* Python3 _(or fork and rewrite in another language)_
* [Selenium Library](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)

## Using the script
* Clone this repository
    - `git clone <repo-link>`
    - `gh repo clone <repo-link>`
* Be in the project folder
    - `cd $HOME/PGCHelper`
* Install the requirements
    - `pip install -r requirements.txt`
* Run the script
    - `python3 pgchelper <target-site> <tld> <target-element-class> <browser>`
    - example: `python3 pgchelper https://mysite.com .com random-button chrome`

## Browser Tests
| Browser Name | Status                        |
|--------------|-------------------------------|
| Firefox      | Working                       |
| Safari       | Not working, unexpected quit. |
| Chrome       | Working                       |
| Edge         | Not Tested                    |

## References
* [Selenium Documentation](https://www.selenium.dev/documentation/)