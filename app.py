from flask import Flask, render_template, redirect, request, flash, session

# from flask import Session
from email import message
from urllib import request
from flask_ngrok import run_with_ngrok


from flask import Flask, render_template
from flask import Flask, redirect, url_for, render_template, request
import requests
import os

app = Flask(__name__)

run_with_ngrok(app)

# session details
app.config["SESSION_TYPE"] = "memcached"
app.config["SECRET_KEY"] = "super secret key"
# sess = Session()


def calculate_avg(credit, grade):
    return credit * grade


def giveGradePoints(grade):
    if grade == "A++":
        return 10
    elif grade == "A+":
        return 9
    elif grade == "A":
        return 8
    elif grade == "B+":
        return 7
    elif grade == "B":
        return 6
    elif grade == "C+":
        return 5
    elif grade == "C":
        return 4
    else:
        return 0


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        select_option = request.form.get("select")
        if select_option == "SEMESTER1":
            return render_template("sem1.html")
        elif select_option == "SEMESTER2":
            return render_template("sem2.html")
        elif select_option == "SEMESTER3":
            return render_template("sem3.html")
        elif select_option == "SEMESTER4":
            return render_template("sem4.html")
        elif select_option == "SEMESTER5":
            return render_template("sem5.html")
        elif select_option == "SEMESTER6":
            return render_template("sem6.html")
        elif select_option == "SEMESTER7":
            return render_template("sem7.html")
        elif select_option == "SEMESTER8":
            return render_template("sem8.html")
        elif select_option == "CGPA":
            return render_template("cgpa.html")
        elif select_option == "SGPA":
            return render_template("sgpa.html")
        else:
            message = "Invalid option"
            return render_template("index.html", message=message)


@app.route("/sem1", methods=["GET", "POST"])
def sem1():
    if request.method == "GET":
        return render_template("sem1.html")
    else:
        total = 22

        em1 = giveGradePoints(request.form.get("sub1"))
        ec = giveGradePoints(request.form.get("sub2"))
        eg = giveGradePoints(request.form.get("sub3"))
        em = giveGradePoints(request.form.get("sub4"))
        bcomit = giveGradePoints(request.form.get("sub5"))
        lab_ec = giveGradePoints(request.form.get("sub6"))
        lab_bcomit = giveGradePoints(request.form.get("sub7"))
        lab_workshop1 = giveGradePoints(request.form.get("sub8"))
        lab_eg = giveGradePoints(request.form.get("sub9"))
        lab_em = giveGradePoints(request.form.get("sub10"))

        sgpa = float(
            (
                float(calculate_avg(4, em1))
                + float(calculate_avg(3, ec))
                + float(calculate_avg(3, eg))
                + float(calculate_avg(3, em))
                + float(calculate_avg(4, bcomit))
                + float(calculate_avg(1, lab_ec))
                + float(calculate_avg(1, lab_bcomit))
                + float(calculate_avg(1, lab_workshop1))
                + float(calculate_avg(1, lab_eg))
                + float(calculate_avg(1, lab_em))
            )
            / total
        )

        message = "Your SGPA is : " + str(sgpa)
        return render_template("sem1.html", message=message)


@app.route("/sem2", methods=["GET", "POST"])
def sem2():
    if request.method == "GET":
        return render_template("sem2.html")
    else:
        total = 22

        em2 = giveGradePoints(request.form.get("sub1"))
        ep = giveGradePoints(request.form.get("sub2"))
        cs = giveGradePoints(request.form.get("sub3"))
        bme = giveGradePoints(request.form.get("sub4"))
        lab_bme = giveGradePoints(request.form.get("sub5"))
        lab_ep = giveGradePoints(request.form.get("sub6"))
        lab_cs = giveGradePoints(request.form.get("sub7"))
        ee = giveGradePoints(request.form.get("sub8"))
        lab_workshop2 = giveGradePoints(request.form.get("sub9"))

        sgpa = float(
            (
                float(calculate_avg(4, em2))
                + float(calculate_avg(3, ep))
                + float(calculate_avg(4, cs))
                + float(calculate_avg(4, bme))
                + float(calculate_avg(1, lab_bme))
                + float(calculate_avg(1, lab_ep))
                + float(calculate_avg(1, lab_cs))
                + float(calculate_avg(3, ee))
                + float(calculate_avg(1, lab_workshop2))
            )
            / total
        )

        message = "Your SGPA is : " + str(sgpa)
        return render_template("sem2.html", message=message)


@app.route("/sem3", methods=["GET", "POST"])
def sem3():
    if request.method == "GET":
        return render_template("sem3.html")
    else:
        total = 22

        em3 = giveGradePoints(request.form.get("sub1"))
        es = giveGradePoints(request.form.get("sub2"))
        oop = giveGradePoints(request.form.get("sub3"))
        dbms = giveGradePoints(request.form.get("sub4"))
        dms = giveGradePoints(request.form.get("sub5"))
        lab_dbms = giveGradePoints(request.form.get("sub6"))
        lab_oop = giveGradePoints(request.form.get("sub7"))
        lab_adv_c_cpp = giveGradePoints(request.form.get("sub8"))
        lab_wt = giveGradePoints(request.form.get("sub9"))

        edp = giveGradePoints(request.form.get("sub10"))
        if edp != 0:
            total = total + 3

        oe2 = giveGradePoints(request.form.get("sub11"))
        if oe2 != 0:
            total = total + 3

        hs = giveGradePoints(request.form.get("sub12"))
        if hs != 0:
            total = total + 2

        sgpa = float(
            (
                float(calculate_avg(4, em3))
                + float(calculate_avg(4, es))
                + float(calculate_avg(3, oop))
                + float(calculate_avg(4, dbms))
                + float(calculate_avg(3, dms))
                + float(calculate_avg(1, lab_dbms))
                + float(calculate_avg(1, lab_oop))
                + float(calculate_avg(1, lab_adv_c_cpp))
                + float(calculate_avg(1, lab_wt))
                + float(calculate_avg(3, edp))
                + float(calculate_avg(3, oe2))
                + float(calculate_avg(2, hs))
            )
            / total
        )

        message = "Your SGPA is : " + str(sgpa)
        return render_template("sem3.html", message=message)


@app.route("/sem4", methods=["GET", "POST"])
def sem4():
    if request.method == "GET":
        return render_template("sem4.html")
    else:
        total = 22

        ds = giveGradePoints(request.form.get("sub1"))
        co = giveGradePoints(request.form.get("sub2"))
        mpi = giveGradePoints(request.form.get("sub3"))
        osst = giveGradePoints(request.form.get("sub4"))
        oe1 = giveGradePoints(request.form.get("sub5"))
        lab_pwp = giveGradePoints(request.form.get("sub6"))
        lab_ds = giveGradePoints(request.form.get("sub7"))
        lab_mpi = giveGradePoints(request.form.get("sub8"))
        lab_jp = giveGradePoints(request.form.get("sub9"))

        oe3 = giveGradePoints(request.form.get("sub10"))
        if oe3 != 0:
            total = total + 3

        hs = giveGradePoints(request.form.get("sub11"))
        if hs != 0:
            total = total + 3

        sgpa = float(
            (
                float(calculate_avg(4, ds))
                + float(calculate_avg(4, co))
                + float(calculate_avg(4, mpi))
                + float(calculate_avg(2, osst))
                + float(calculate_avg(3, oe1))
                + float(calculate_avg(1, lab_pwp))
                + float(calculate_avg(1, lab_ds))
                + float(calculate_avg(1, lab_mpi))
                + float(calculate_avg(2, lab_jp))
                + float(calculate_avg(3, oe3))
                + float(calculate_avg(3, hs))
            )
            / total
        )

        message = "Your SGPA is : " + str(sgpa)
        return render_template("sem4.html", message=message)


@app.route("/sem5", methods=["GET", "POST"])
def sem5():
    if request.method == "GET":
        return render_template("sem5.html")
    else:
        total = 24
        daa = giveGradePoints(request.form.get("sub1"))
        os = giveGradePoints(request.form.get("sub2"))
        toc = giveGradePoints(request.form.get("sub3"))
        se = giveGradePoints(request.form.get("sub4"))
        dmdw = giveGradePoints(request.form.get("sub5"))
        lab_daa = giveGradePoints(request.form.get("sub6"))
        lab_os = giveGradePoints(request.form.get("sub7"))
        lab_dmdw = giveGradePoints(request.form.get("sub8"))
        miniproject = giveGradePoints(request.form.get("sub9"))
        pe1 = giveGradePoints(request.form.get("sub10"))
        lab_pe1 = giveGradePoints(request.form.get("sub11"))
        if pe1 != 0:
            total = total + 5
        else:
            lab_pe1 = 0
        pe2 = giveGradePoints(request.form.get("sub12"))
        lab_pe2 = giveGradePoints(request.form.get("sub13"))
        if pe2 != 0:
            total = total + 5
        else:
            lab_pe2 = 0

        print(daa)
        print(os)
        print(toc)
        print(se)
        print(dmdw)
        print(lab_daa)
        print(lab_os)
        print(lab_dmdw)
        print(miniproject)
        print(pe1)
        print(lab_pe1)
        print(pe2)
        print(lab_pe2)
        print(total)

        sgpa = float(
            (
                float(calculate_avg(4, daa))
                + float(calculate_avg(3, os))
                + float(calculate_avg(4, toc))
                + float(calculate_avg(4, se))
                + float(calculate_avg(4, dmdw))
                + float(calculate_avg(1, lab_daa))
                + float(calculate_avg(1, lab_os))
                + float(calculate_avg(1, lab_dmdw))
                + float(calculate_avg(2, miniproject))
                + float(calculate_avg(4, pe1))
                + float(calculate_avg(1, lab_pe1))
                + float(calculate_avg(4, pe2))
                + float(calculate_avg(1, lab_pe2))
            )
            / total
        )

        message = "Your SGPA is : " + str(sgpa)
        return render_template("sem5.html", message=message)


@app.route("/sem6", methods=["GET", "POST"])
def sem6():
    if request.method == "GET":
        return render_template("sem6.html")
    else:
        total = 19
        cn = giveGradePoints(request.form.get("sub1"))
        spcc = giveGradePoints(request.form.get("sub2"))
        aa = giveGradePoints(request.form.get("sub3"))
        ds = giveGradePoints(request.form.get("sub4"))
        lab_adt = giveGradePoints(request.form.get("sub5"))
        lab_cn = giveGradePoints(request.form.get("sub6"))
        lab_aa = giveGradePoints(request.form.get("sub7"))
        lab_ds = giveGradePoints(request.form.get("sub8"))
        seminar = giveGradePoints(request.form.get("sub9"))
        pe3 = giveGradePoints(request.form.get("sub10"))
        lab_pe3 = giveGradePoints(request.form.get("sub11"))
        if pe3 != 0:
            total = total + 5
        else:
            lab_pe3 = 0
        pe4 = giveGradePoints(request.form.get("sub12"))
        lab_pe4 = giveGradePoints(request.form.get("sub13"))
        if pe4 != 0:
            total = total + 5
        else:
            lab_pe4 = 0

        sgpa = float(
            (
                float(calculate_avg(3, cn))
                + float(calculate_avg(4, spcc))
                + float(calculate_avg(3, aa))
                + float(calculate_avg(4, ds))
                + float(calculate_avg(1, lab_adt))
                + float(calculate_avg(1, lab_cn))
                + float(calculate_avg(1, lab_aa))
                + float(calculate_avg(1, lab_ds))
                + float(calculate_avg(1, seminar))
                + float(calculate_avg(4, pe3))
                + float(calculate_avg(1, lab_pe3))
                + float(calculate_avg(4, pe4))
                + float(calculate_avg(1, lab_pe4))
            )
            / total
        )

        message = "Your SGPA is : " + str(sgpa)
        return render_template("sem6.html", message=message)


@app.route("/sem7", methods=["GET", "POST"])
def sem7():

    if request.method == "GET":
        return render_template("sem7.html")

    else:

        total = 5

        bdp = giveGradePoints(request.form.get("sub1"))

        hs = giveGradePoints(request.form.get("sub2"))
        if hs != 0:
            total = total + 2

        oe3 = giveGradePoints(request.form.get("sub3"))
        if oe3 != 0:
            total = total + 3

        pe1 = giveGradePoints(request.form.get("sub4"))
        lab_pe1 = giveGradePoints(request.form.get("sub5"))
        if pe1 != 0:
            total = total + 5
        else:
            lab_pe1 = 0

        pe2 = giveGradePoints(request.form.get("sub6"))
        lab_pe2 = giveGradePoints(request.form.get("sub7"))
        if pe2 != 0:
            total = total + 5
        else:
            lab_pe2 = 0

        project1 = giveGradePoints(request.form.get("sub8"))

        sgpa = float(
            (
                float(calculate_avg(3, bdp))
                + float(calculate_avg(2, hs))
                + float(calculate_avg(3, oe3))
                + float(calculate_avg(4, pe1))
                + float(calculate_avg(1, lab_pe1))
                + float(calculate_avg(4, pe2))
                + float(calculate_avg(1, lab_pe2))
                + float(calculate_avg(2, project1))
            )
            / total
        )

        message = "Your SGPA is : " + str(sgpa)
        return render_template("sem7.html", message=message)


@app.route("/sem8", methods=["GET", "POST"])
def sem8():

    if request.method == "GET":
        return render_template("sem8.html")

    else:

        total = 6

        hs1 = giveGradePoints(request.form.get("sub1"))
        if hs1 != 0:
            total = total + 3

        oe4 = giveGradePoints(request.form.get("sub2"))
        if oe4 != 0:
            total = total + 3

        pe3 = giveGradePoints(request.form.get("sub3"))
        lab_pe3 = giveGradePoints(request.form.get("sub4"))
        if pe3 != 0:
            total = total + 5
        else:
            lab_pe3 = 0

        pe4 = giveGradePoints(request.form.get("sub5"))
        lab_pe4 = giveGradePoints(request.form.get("sub6"))
        if pe4 != 0:
            total = total + 5
        else:
            lab_pe4 = 0

        project2 = giveGradePoints(request.form.get("sub7"))

        sgpa = float(
            (
                float(calculate_avg(3, hs1))
                + float(calculate_avg(3, oe4))
                + float(calculate_avg(4, pe3))
                + float(calculate_avg(1, lab_pe3))
                + float(calculate_avg(4, pe4))
                + float(calculate_avg(1, lab_pe4))
                + float(calculate_avg(6, project2))
            )
            / total
        )

        message = "Your SGPA is : " + str(sgpa)
        return render_template("sem8.html", message=message)


@app.route("/sgpa", methods=["GET", "POST"])
def calculate_sgpa():
    if request.method == "POST":
        total = 0
        total_credit = 0
        for key in request.form:
            if key.startswith("subject_"):
                index = key.split("_")[1]
                subject = giveGradePoints(request.form.get(key))
                credit = request.form.get("credit_" + index)
                total = total + float(subject) * float(credit)
                total_credit = total_credit + float(credit)
                message = "Your SGPA is " + str (total / total_credit)
        return render_template("sgpa.html", message=message)

    else:
        return render_template("sgpa.html")


@app.route("/cgpa", methods=["GET", "POST"])
def calculate_cgpa():
    if request.method == "POST":
        total = 0
        total_credit = 0
        for key in request.form:
            if key.startswith("sgpa_"):
                index = key.split("_")[1]
                sgpa = request.form.get(key)
                credit = request.form.get("credit_" + index)
                total = total + float(sgpa) * float(credit)
                total_credit = total_credit + float(credit)
                message = "Your CGPA is " + str (total / total_credit)
        return render_template("cgpa.html", message=message)

    else:
        return render_template("cgpa.html")


# if __name__ == "__main__":
#     app.run(debug=True)
