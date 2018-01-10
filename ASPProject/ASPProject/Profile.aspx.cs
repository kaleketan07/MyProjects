using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Net.Mail;
using System.Data;

namespace ASPProject
{
    public partial class WebForm3 : System.Web.UI.Page
    {
        string j;
        protected void Page_Load(object sender, EventArgs e)
        {
            LinqtoSQLDataContext datac = new LinqtoSQLDataContext();
            
            if (Session["UserName"] != null)
            {
                namelbl.Text = Session["UserName"].ToString();
            }
            var x = from b in datac.details
                    where b.Fnm == namelbl.Text
                    select b.eno;
             j = x.FirstOrDefault();
            Name1.Text = j;

            //HttpCookie cookie = new HttpCookie("LoginInfo");
            //cookie=Request.Cookies["LoginInfo"];
            //if (cookie != null)
            //{
            //    namelbl.Text = cookie.Value;
            //}
            //else 
            //{
            //    namelbl.Text = "Mr.X";
            //}
            //String enr = Request.QueryString["Enroll"].ToString();
            //namelbl.Text = enr;

           
        }

        protected void post_Click(object sender, EventArgs e)
        {
            LinqtoSQLDataContext datac = new LinqtoSQLDataContext();
            var c = from p in datac.details
                    where p.Fnm == namelbl.Text
                    select p.email;
            string s = c.FirstOrDefault();

           
            complaint cmp = new complaint
            {
                Comp = TextBox1.Text,
                Enr = j,
            };
            datac.complaints.InsertOnSubmit(cmp);
            try
            {
                datac.SubmitChanges();
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);
                datac.SubmitChanges();
            }
            if (s != null)
            {
                SendEmail(s);
            }
            else
            {
                Response.Redirect("Errorpage.aspx");
            }
            TextBox1.Text = "";
            //Name.Text = "";
        }

        public void SendEmail(string s)
        {
            MailMessage mm = new MailMessage("myemail@something.com", s);
            mm.Subject = "Thanks for using the complaint redressal portal";
            mm.Body = "Your complaint has been registered! And is being processed. We will revert back shortly.";

            SmtpClient sc = new SmtpClient("smtp.gmail.com", 587);
            sc.Credentials = new System.Net.NetworkCredential()
            {
                UserName="myemail@something.com",
                Password="mypassword"
            };

           sc.EnableSsl=true;
            sc.Send(mm);
        }

        protected void Name_TextChanged(object sender, EventArgs e)
        {

        }

        protected void Logout_Click(object sender, EventArgs e)
        {
            Server.Transfer("Default.aspx");
        }
    }
}