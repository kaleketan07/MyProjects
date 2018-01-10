<%@ Page Title="" Language="C#" MasterPageFile="~/Master1.Master" AutoEventWireup="true" CodeBehind="Registration.aspx.cs" Inherits="ASPProject.WebForm2" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
    <title>Registration Form</title>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
    <br />
    <div class="container">
            <h5><u>Please fill in your details:</u></h5>
            <h5 align="center">
                    <asp:Label ID="Label1" runat="server"></asp:Label>
            </h5>
        <div class="row">
            <div class="input-field col s6">
                <i class="fa fa-user"></i>
                <asp:TextBox  TextMode="SingleLine" ID="Fname" runat="server" class="validate"></asp:TextBox>
                
                <label for="icon_prefix">
                    First Name</label>
            </div>
            <div class="input-field col s6">
                <i class="fa fa-user"></i>
                <asp:TextBox ID="Lname" TextMode="SingleLine" runat="server" class="validate"></asp:TextBox>
                
                <label for="icon_prefix">
                    Last Name
                 </label>
            </div>
            <div class="input-field col s6">
                <i class="fa fa-registered"></i>
                <asp:TextBox ID="rno" TextMode="SingleLine" runat="server" class="validate"></asp:TextBox>
                
                <label for="icon_prefix">
                    Enrollment Number
                </label>
                <asp:RequiredFieldValidator ID="RequiredFieldValidator1" runat="server" ControlToValidate="rno" ErrorMessage="This is a required field" ForeColor="Red"></asp:RequiredFieldValidator>
            </div>
            
           
                <div class="input-field col s6">
                    <i class="fa fa-phone"></i>
                    <asp:TextBox ID="telephone" TextMode="Phone" runat="server" class="validate"></asp:TextBox>
                    <label for="telephone">
                        Mobile
                    </label>
                </div>
                <div class="input-field col s6">
                    <i class="fa fa-envelope"></i>
                    <asp:TextBox ID="Mail" runat="server" class="validate"></asp:TextBox>
                    <label for="icon_prefix">
                        E-mail id
                    </label>
                    <asp:RequiredFieldValidator ID="RequiredFieldValidator2" runat="server" ControltoValidate="Mail" ErrorMessage="This is a required field" ForeColor="Red"></asp:RequiredFieldValidator>
                </div>
                <div class="input-field col s6">
                    <i class="fa fa-lock"></i>
                    <asp:TextBox ID="Pass" Textmode="Password"  runat="server" class="validate"></asp:TextBox>
                    <label for="icon_prefix">
                        Password
                    </label>
                </div>
                <div class="input-field col s6">
                    <i class="fa fa-lock"></i>
                    <asp:TextBox ID="ReEnterPass" TextMode=Password runat="server" class="validate"></asp:TextBox>
                     <asp:CompareValidator ID="CompareValidatorpassword"  
                        ControlToValidate="ReEnterPass" ControlToCompare="Pass" runat="server" 
                        ErrorMessage="password and re-enter password do not match" Type="String" Operator="Equal" ForeColor="Red">
                     </asp:CompareValidator>
                    <label for="icon_prefix">
                        Re-Enter Password</label>
                </div>
            </div>
            <div class="row">
                <div class="col s6">
                    <asp:Button ID="Submit" runat="server" CausesValidation="true" Text="Submit" class="btn-large waves-effect waves-light teal lighten-1"
                        align="center" onclick="Submit_Click" />
                </div>
            </div>
        </div>
</asp:Content>
