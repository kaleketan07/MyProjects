<%@ Page Title="" Language="C#" MasterPageFile="~/Master1.Master" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="ASPProject.WebForm1" %>
<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server">
    <title>Home</title>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" runat="server">
     <div id="index-banner" class="parallax-container">
        <div class="section no-pad-bot">
            <div class="container">
                <br>
                <br>
                <h1 class="header center white-text text-lighten-2">
                    Student Grievance Redressal Portal</h1>
                <div class="row center">
                    <h5 class="header col s12 light">
                        &nbsp</h5>
                    <h5 class="header col s12 light white-text">
                        A portal where your complaints get resolved</h5>
                </div>
                <br />
                <br />
            </div>
        </div>
        <div class="parallax">
            <img src="images/26.jpg" alt="Unsplashed background img 1" />
        </div>
    </div>
    <div class="container">
        <div class="section">
            <!--   Icon Section   -->
            <div class="row">
                <div class="col s12 m4">
                    <div class="icon-block">
                        <h2 class="center brown-text">
                            <span class="fa fa-flash"></span></h2>
                        <h5 class="center">
                            Speeds up development</h5>
                        <p class="light">
                            We believe that grievances are the most serious obstruction in the path to development. Students are the strength of the institution. So their grievances must be resolved immediately.  </p>
                    </div>
                </div>
                <div class="col s12 m4">
                    <div class="icon-block">
                        <h2 class="center brown-text">
                            <i class="fa fa-group"></i></h2>
                        <h5 class="center">
                            User Experience Focused</h5>
                        <p class="light">
                            This is an extremely user friendly portal for grievance redressal of the students. All aspects of this portal are designed keeping in mind the improved user experience</p>
                    </div>
                </div>
                <div class="col s12 m4">
                    <div class="icon-block">
                        <h2 class="center brown-text">
                            <span class="fa fa-gear"></span></h2>
                        <h5 class="center">
                            Easy to work with</h5>
                        <p class="light">
                            We have provided detailed documentation and authentication to ensure that this process gets smoother. NO Paper work, NO Time wastage.This portal allows the students to share their grievances with the institution anytime and from anywhere </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="parallax-container valign-wrapper">
        <%--<div class="section no-pad-bot">
            <div class="container">
                <div class="row center">
                    <h5 class="header col s12 light white-text">
                        Sign up to get started! Don't let any grief be unresolved. 
                    </h5>
                </div>
            </div>
        </div>--%>
        <div class="parallax">
            <img src="images/8.jpg" alt="Unsplashed background img 2">
        </div>
    </div>
    <div class="container">
        <div class="section">
            <div class="row">
                <div class="col s12 center">
                    <h3>
                        Sign In/Sign Up
                    </h3>
                </div>
                <div class="row">
                    <div class="row">
                        <div class="input-field col s6">
                            <asp:TextBox ID="txtName" runat="server" class="validate"></asp:TextBox>
                            <asp:RequiredFieldValidator ID="RequiredFieldValidator1" runat="server" ErrorMessage="Please Enter name" ControlToValidate="txtName" ForeColor="Red"></asp:RequiredFieldValidator>
                            <label class="active">
                                Name 
                            </label>
                &nbsp;  </div>
                    </div>
                    <div class="row">
                        <div class="input-field col s6">
                            <asp:TextBox ID="Password" Textmode="password" runat="server" class="validate"></asp:TextBox>
                            <asp:RequiredFieldValidator ID="RequiredFieldValidator2" runat="server" ErrorMessage="Please Enter the password" ControlToValidate="Password" ForeColor="Red" ></asp:RequiredFieldValidator>
                            <label class="active" for="first_name2">
                                     Password</label>
                        </div>
                    </div>
                    <div>
                        <asp:ScriptManager ID="ScriptManager1" runat="server">
                        </asp:ScriptManager>
                        <asp:UpdatePanel ID="UpdatePanel1" runat="server">
                            <ContentTemplate>
                                <asp:Label ID="Errorlbl" runat="server" Text=""></asp:Label>
                            </ContentTemplate>
                        </asp:UpdatePanel>
                    </div>
                    <asp:Button ID="Submit" runat="server" Text="Submit" 
                        class="btn-large waves-effect waves-light teal" onclick="Submit_Click" 
                         />&nbsp;
                    
                    <asp:Button ID="SignUp" runat="server" CausesValidation="false"  Text="Sign Up" class="btn-large waves-effect waves-light teal lighten-1" 
                        onclick="SignUp_Click" ToolTip="create an account" />
                </div>
            </div>
        </div>
    </div>
</asp:Content>
