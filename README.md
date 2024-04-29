# Coolsign

Coolsign is a free solution for employee attendance in [Odoo](https://www.odoo.com/) 17. Using it, an employee can easily check in and out using his or her smartphone, and the detected location will be saved in the attendance record. Coolsign consists of a backend part, the hr_coolsign custom module, and a frontend one, an Android app.

## Odoo custom module

![coolsign-odoo-module](https://github.com/apmatic/coolsign/assets/168338449/c522201c-4385-418d-a0fa-c3cdc5e7d11e)

The custom module, once installed, creates a Coolsign tab in the employee form, containing two fields. With the first, **Enable Coolsign App**, the HR Manager can enable or disable the use of the app for that employee.
The second one, **Coolsign App ID**, records the ID which uniquely identifies the smartphone. If the employee configured the app on another smartphone, the ID would change so only one smartphone can be used by the employee at any given time.

![coolsign-odoo-employee](https://github.com/apmatic/coolsign/assets/168338449/1ee13a4a-646a-461a-adc6-adf7c5553fff)

## Coolsign Android app

The Coolsign Android app is available here as an apk file ready to be installed. Three screenshots of the app follow:

### Main page

![coolsign-main-border](https://github.com/apmatic/coolsign/assets/168338449/f2d76b4f-9f0f-4550-aecc-276d28b12d4c)

### Map page

![coolsign-map-border](https://github.com/apmatic/coolsign/assets/168338449/cd2980d8-ccda-46f9-a3ea-0a1f77f51b4c)

### Settings page

![coolsign-settings-border](https://github.com/apmatic/coolsign/assets/168338449/96d0b4eb-5a79-47e4-af2a-66879d3c7b78)

### Configuration

In the Coolsign app **Settings** page the login credentials must be specified. In a production environment the **Hostname** is usually something like `https://odoo.companyname.com`. If you are a developer and Odoo is running on your developer box, use the LAN IP followed by the port, for example `http://192.168.1.2:8069`.

Also, login and password of the user related to the employee is needed in order to establish a connection to Odoo - employees without the associated user cannot connect to Odoo. Remember that, instead of the password, you can use an API key: create one from **Account Security** of your Odoo Profile.

![coolsign-odoo-my-profile](https://github.com/apmatic/coolsign/assets/168338449/9a91b471-5cb8-473f-ade7-b8d7ad05b5b4)

![coolsign-odoo-api-key](https://github.com/apmatic/coolsign/assets/168338449/d16a51d7-28a8-4a8f-baf3-1cfb37947cca)
