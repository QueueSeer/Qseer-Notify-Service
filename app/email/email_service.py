from app.core.config import settings
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.message import EmailMessage

def send_email(header:str,body_header1:str,body_header2:str,body:str,button_text:str,button_link:str,email:str):
    port = 465  # For SSL
    smtp_server = settings.smtp_SERVER
    sender_email = settings.smtp_LOGIN  # Enter your address
    receiver_email = email  # Enter receiver address
    password = settings.smtp_PASSWORD
    message = EmailMessage()
    message['Subject'] = header
    message['From'] = sender_email
    message['To'] = receiver_email
    h1 = body_header1
    h2 = body_header2

    message.set_content('''
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="x-apple-disable-message-reformatting">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title></title>

  <style type="text/css">
    @media only screen and (min-width: 620px) {
      .u-row {
        width: 600px !important;
      }

      .u-row .u-col {
        vertical-align: top;
      }


      .u-row .u-col-100 {
        width: 600px !important;
      }

    }

    @media only screen and (max-width: 620px) {
      .u-row-container {
        max-width: 100% !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
      }

      .u-row {
        width: 100% !important;
      }

      .u-row .u-col {
        display: block !important;
        width: 100% !important;
        min-width: 320px !important;
        max-width: 100% !important;
      }

      .u-row .u-col>div {
        margin: 0 auto;
      }


    }

    body {
      margin: 0;
      padding: 0
    }

    table,
    td,
    tr {
      border-collapse: collapse;
      vertical-align: top
    }

    p {
      margin: 0
    }

    .ie-container table,
    .mso-container table {
      table-layout: fixed
    }

    * {
      line-height: inherit
    }

    a[x-apple-data-detectors=true] {
      color: inherit !important;
      text-decoration: none !important
    }


    table,
    td {
      color: #000000;
    }

    #u_body a {
      color: #73087f;
      text-decoration: underline;
    }

    @media (max-width: 480px) {
      #u_content_heading_2 .v-font-size {
        font-size: 20px !important;
      }

      #u_content_text_1 .v-container-padding-padding {
        padding: 10px !important;
      }

      #u_content_button_1 .v-size-width {
        width: 65% !important;
      }

      #u_content_button_1 .v-container-padding-padding {
        padding: 10px 10px 40px !important;
      }
    }
  </style>



  <link href="https://fonts.googleapis.com/css?family=Raleway:400,700&display=swap" rel="stylesheet" type="text/css">

</head>

<body class="clean-body u_body"
  style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #e7e7e7;color: #000000">
  <table id="u_body"
    style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #e7e7e7;width:100%"
    cellpadding="0" cellspacing="0">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">



          <div class="u-row-container" style="padding: 0px;background-color: transparent">
            <div class="u-row"
              style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
              <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0"
                width="100%" border="0">
                <tbody>
                  <tr>
                    <td class="v-container-padding-padding"
                      style="overflow-wrap:break-word;word-break:break-word;padding:20px 0px;font-family:arial,helvetica,sans-serif;"
                      align="left">

                      <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%"
                        style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                        <tbody>
                          <tr style="vertical-align: top">
                            <td
                              style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                              <span>&#160;</span>
                            </td>
                          </tr>
                        </tbody>
                      </table>

                    </td>
                  </tr>
                </tbody>
              </table>
              <div
                style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">

                <div class="u-col u-col-100"
                  style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                  <div
                    style="background-color: #e9e9e9;height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                    <div
                      style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                    </div>
                  </div>
                </div>
              </div>
            </div>





            <div class="u-row-container" style="padding: 0px;background-color: transparent">
              <div class="u-row"
                style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                <div
                  style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">

                  <div class="u-col u-col-100"
                    style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                    <div style="background-color: #ffffff;height: 100%;width: 100% !important;">
                      <div
                        style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

                        <table id="u_content_heading_2" style="font-family:arial,helvetica,sans-serif;"
                          role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                          <tbody>
                            <tr>

                              <td class="v-container-padding-padding"
                                style="overflow-wrap:break-word;word-break:break-word;padding:20px 10px 10px;font-family:arial,helvetica,sans-serif;"
                                align="left">

                                <h1 class="v-font-size"
                                  style="margin: 0px; line-height: 140%; text-align: center; word-wrap: break-word; font-size: 25px; font-weight: 400;">
                                  <span>'''+h1+'''<br />'''+h2+'''</span>
                                </h1>

                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                          cellspacing="0" width="100%" border="0">
                          <tbody>
                            <tr>
                              <td class="v-container-padding-padding"
                                style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                                align="left">

                                <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0"
                                  width="19%"
                                  style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 5px solid #c554f2;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                  <tbody>
                                    <tr style="vertical-align: top">
                                      <td
                                        style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                        <span>&#160;</span>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>

                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <table id="u_content_text_1" style="font-family:arial,helvetica,sans-serif;" role="presentation"
                          cellpadding="0" cellspacing="0" width="100%" border="0">
                          <tbody>
                            <tr>
                              <td class="v-container-padding-padding"
                                style="overflow-wrap:break-word;word-break:break-word;padding:10px 60px;font-family:arial,helvetica,sans-serif;"
                                align="left">

                                <div class="v-font-size"
                                  style="font-size: 14px; color: #616161; line-height: 140%; text-align: center; word-wrap: break-word;">
                                  <p style="line-height: 140%;"><span
                                      style="font-family: Raleway, sans-serif; line-height: 19.6px;">'''+body+'''</span></p>
                                </div>

                              </td>
                            </tr>
                          </tbody>
                        </table>

                        <table id="u_content_button_1" style="font-family:arial,helvetica,sans-serif;"
                          role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                          <tbody>
                            <tr>
                              <td class="v-container-padding-padding"
                                style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 60px;font-family:arial,helvetica,sans-serif;"
                                align="left">

                                <div align="center">
                                  <a href="'''+button_link+'''" target="_blank"
                                    class="v-button v-size-width v-font-size"
                                    style="box-sizing: border-box;display: inline-block;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #c554f2; border-radius: 4px;-webkit-border-radius: 4px; -moz-border-radius: 4px; width:31%; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;font-size: 14px;">
                                    <span style="display:block;padding:10px 20px;line-height:120%;"><span
                                        style="font-size: 14px; line-height: 16.8px;">'''+button_text+'''</span></span>
                                  </a>
                                </div>

                              </td>
                            </tr>
                          </tbody>
                        </table>

                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>





            <div class="u-row-container" style="padding: 0px;background-color: transparent">
              <div class="u-row"
                style="margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
                <div
                  style="border-collapse: collapse;display: table;width: 100%;height: 100%;background-color: transparent;">


                  <div class="u-col u-col-100"
                    style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                    <div
                      style="height: 100%;width: 100% !important;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">
                      <div
                        style="box-sizing: border-box; height: 100%; padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;border-radius: 0px;-webkit-border-radius: 0px; -moz-border-radius: 0px;">

                        <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                          cellspacing="0" width="100%" border="0">
                          <tbody>
                            <tr>
                              <td class="v-container-padding-padding"
                                style="overflow-wrap:break-word;word-break:break-word;padding:20px 0px;font-family:arial,helvetica,sans-serif;"
                                align="left">

                                <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0"
                                  width="100%"
                                  style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                  <tbody>
                                    <tr style="vertical-align: top">
                                      <td
                                        style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                        <span>&#160;</span>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>

                              </td>
                            </tr>
                          </tbody>
                        </table>

                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>



        </td>
      </tr>
    </tbody>
  </table>
</body>

</html>
    ''', subtype='html')

    context = ssl.create_default_context()
    try :
      with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        #server.sendmail(sender_email, receiver_email, message)
        server.send_message(message)
    except Exception as e:
      return False
    return True