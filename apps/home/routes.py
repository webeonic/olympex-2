# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index', active_menu='dashboard')




# dashboard dropdown

@blueprint.route('/dashboards-discover/')
def dashboards_discover():
  return render_template('home/dashboards-discover.html', segment='dashboards_discover', active_menu='dashboard')


@blueprint.route('/dashboards-sales/')
def dashboards_sales():
  return render_template('home/dashboards-sales.html', segment='dashboards_sales', active_menu='dashboard')


@blueprint.route('/dashboards-automotive/')
def dashboards_automotive():
  return render_template('home/dashboards-automotive.html', segment='dashboards_automotive', active_menu='dashboard')


@blueprint.route('/dashboards-smart/')
def dashboards_smart():
  return render_template('home/dashboards-smart-home.html', segment='dashboards_smart', active_menu='dashboard')


# pages all dropdown menus


# Profile
@blueprint.route('/profile-overview/')
def profile_overview():
  return render_template('home/profile-overview.html', parent="profile", segment='profile_overview', active_menu='pages')

@blueprint.route('/profile-projects/')
def profile_projects():
  return render_template('home/profile-projects.html',parent="profile", segment='profile_projects', active_menu='pages')

@blueprint.route('/profile-messages/')
def profile_messages():
  return render_template('home/profile-messages.html',parent="profile", segment='profile_messages', active_menu='pages')


# User
@blueprint.route('/users-reports/')
def users_reports():
  return render_template('home/users-reports.html', parent="user", segment='users_reports', active_menu='pages')

@blueprint.route('/new-user/')
def new_user():
  return render_template('home/users-new-user.html',parent="user", segment='new_user', active_menu='pages')



# Account
@blueprint.route('/account-settings/')
def account_settings():
  return render_template('home/account-settings.html', parent="account", segment='account_settings', active_menu='pages')

@blueprint.route('/account-billing/')
def account_billing():
  return render_template('home/account-billing.html',parent="account", segment='account_billing', active_menu='pages')

@blueprint.route('/account-invoice/')
def account_invoice():
  return render_template('home/account-invoice.html', parent="account", segment='account_invoice', active_menu='pages')

@blueprint.route('/account-security/')
def account_security():
  return render_template('home/account-security.html',parent="account", segment='account_security', active_menu='pages')


# Projects
@blueprint.route('/projects-general/')
def projects_general():
  return render_template('home/projects-general.html', parent="projects", segment='projects_general', active_menu='pages')

@blueprint.route('/projects-timeline/')
def projects_timeline():
  return render_template('home/projects-timeline.html',parent="projects", segment='projects_timeline', active_menu='pages')

@blueprint.route('/projects-new-project/')
def projects_new_project():
  return render_template('home/projects-new-project.html', parent="projects", segment='projects_new_project', active_menu='pages')


# Virtual Reality
@blueprint.route('/vr-default/')
def vr_default():
  return render_template('home/vr-default.html', parent="vr", segment='vr_default', active_menu='pages')

@blueprint.route('/vr-info/')
def vr_info():
  return render_template('home/vr-info.html',parent="vr", segment='vr-info', active_menu='pages')

# single page
@blueprint.route('/pricing-page/')
def pricing_page():
  return render_template('home/pricing-page.html', parent="pricing-page", segment='pricing_page', active_menu='pages')

@blueprint.route('/rtl-page/')
def rtl_page():
  return render_template('home/rtl-page.html',parent="rtl-page", segment='rtl-page', active_menu='pages')

@blueprint.route('/widgets/')
def widgets():
  return render_template('home/widgets.html', parent="widgets", segment='widgets', active_menu='pages')

@blueprint.route('/charts/')
def charts():
  return render_template('home/charts.html',parent="charts", segment='charts', active_menu='pages')

@blueprint.route('/sweet-alerts/')
def sweet_alerts():
  return render_template('home/sweet-alerts.html', parent="sweet-alerts", segment='sweet_alerts', active_menu='pages')

@blueprint.route('/notifications/')
def notifications():
  return render_template('home/notifications.html',parent="notifications", segment='notifications', active_menu='pages')


# application page
@blueprint.route('/applications-crm/')
def applications_crm():
  return render_template('home/applications-crm.html',parent="applications",  segment='applications_crm', active_menu='applications')

@blueprint.route('/applications-kanban/')
def applications_kanban():
  return render_template('home/applications-kanban.html',parent="applications", segment='applications_kanban', active_menu='applications')

@blueprint.route('/applications-wizard/')
def applications_wizard():
  return render_template('home/applications-wizard.html',parent="applications",segment='applications_wizard', active_menu='applications')

@blueprint.route('/applications-datatables/')
def applications_datatables():
  return render_template('home/applications-datatables.html',parent="applications", segment='applications_datatables', active_menu='applications')

@blueprint.route('/applications-calendar/')
def applications_calendar():
  return render_template('home/applications-calendar.html',parent="applications", segment='applications_calendar', active_menu='applications')

@blueprint.route('/applications-stats/')
def applications_stats():
  return render_template('home/applications-stats.html',parent="applications", segment='applications_stats', active_menu='applications')


# Ecommerce page

# Products
@blueprint.route('/ecommerce-product-new/')
def ecommerce_product_new():
  return render_template('home/ecommerce-product-new.html', parent='ecommerce-product',  segment='ecommerce_product_new', active_menu='ecommerce')

@blueprint.route('/ecommerce-product-edit/')
def ecommerce_product_edit():
  return render_template('home/ecommerce-product-edit.html',parent='ecommerce-product', segment='ecommerce_product_edit', active_menu='ecommerce')

@blueprint.route('/ecommerce-product-page/')
def ecommerce_product_page():
  return render_template('home/ecommerce-product-page.html',parent='ecommerce-product', segment='ecommerce_product_page', active_menu='ecommerce')

@blueprint.route('/ecommerce-products-list/')
def ecommerce_products_list():
  return render_template('home/ecommerce-products-list.html',parent='ecommerce-product', segment='ecommerce_products_list', active_menu='ecommerce')


# Order
@blueprint.route('/ecommerce-orders-list/')
def ecommerce_orders_list():
  return render_template('home/ecommerce-orders-list.html', parent='ecommerce-orders',  segment='ecommerce_orders_list', active_menu='ecommerce')

@blueprint.route('/ecommerce-orders-details/')
def ecommerce_orders_details():
  return render_template('home/ecommerce-orders-details.html',parent='ecommerce-orders', segment='ecommerce_orders_details', active_menu='ecommerce')

# Referral
@blueprint.route('/ecommerce-referral/')
def ecommerce_referral():
  return render_template('home/ecommerce-referral.html', segment='ecommerce_referral', active_menu='ecommerce')



# Authentication

# Sign in
@blueprint.route('/signin-basic/')
def signin_basic():
  return render_template('home/authentication-signin-basic.html',   segment='signin_basic', )

@blueprint.route('/signin-cover/')
def signin_cover():
  return render_template('home/authentication-signin-cover.html',segment='signin_cover')

@blueprint.route('/signin-illustration/')
def signin_illustration():
  return render_template('home/authentication-signin-illustration.html',segment='signin_illustration')




# Sign up
@blueprint.route('/signup-basic/')
def signup_basic():
  return render_template('home/authentication-signup-basic.html',segment='signup-basic')

@blueprint.route('/signup-cover/')
def signup_cover():
  return render_template('home/authentication-signup-cover.html', segment='signup_cover')

@blueprint.route('/signup-illustration/')
def signup_illustration():
  return render_template('home/authentication-signup-illustration.html', segment='signup-illustration')

# Reset Password
@blueprint.route('/reset-basic/')
def reset_basic():
  return render_template('home/authentication-reset-basic.html',   segment='reset_basic')

@blueprint.route('/reset-cover/')
def reset_cover():
  return render_template('home/authentication-reset-cover.html',segment='reset_cover')

@blueprint.route('/reset-illustration/')
def reset_illustration():
  return render_template('home/authentication-reset-illustration.html',segment='reset_illustration')


# Lock 
@blueprint.route('/lock-basic/')
def lock_basic():
  return render_template('home/authentication-lock-basic.html',segment='lock_basic')

@blueprint.route('/lock-cover/')
def lock_cover():
  return render_template('home/authentication-lock-cover.html', segment='lock_cover')

@blueprint.route('/lock-illustration/')
def lock_illustration():
  return render_template('home/authentication-lock-illustration.html',segment='lock_illustration')


# 2-Step Verification
@blueprint.route('/verification-basic/')
def verification_basic():
  return render_template('home/authentication-verification-basic.html', segment='verification_basic')

@blueprint.route('/verification-cover/')
def verification_cover():
  return render_template('home/authentication-verification-cover.html', segment='verification_cover')

@blueprint.route('/verification-illustration/')
def verification_illustration():
  return render_template('home/authentication-verification-illustration.html', segment='verification_illustration')

# Error
@blueprint.route('/page-404/')
def page_404():
  return render_template('home/page-404.html',  segment='page_404')

@blueprint.route('/page-500/')
def page_500():
  return render_template('home/page-500.html', segment='page_500')



@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment, active_menu = get_segment( request )

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template( 'home/' + template, segment=segment, active_menu=active_menu )

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment( request ): 

    try:

        segment     = request.path.split('/')[-1]
        active_menu = None

        if segment == '':
            segment     = 'index'
            active_menu = 'dashboard'

        if segment.startswith('dashboards-'):
            active_menu = 'dashboard'

        if segment.startswith('account-') or segment.startswith('users-') or segment.startswith('profile-') or segment.startswith('projects-') or segment.startswith('virtual-'):
            active_menu = 'pages'

        if  segment.startswith('notifications') or segment.startswith('sweet-alerts') or segment.startswith('charts.html') or segment.startswith('widgets') or segment.startswith('pricing'):
            active_menu = 'pages'

        if  segment.startswith('applications'):    
            active_menu = 'apps'

        return segment, active_menu     

    except:
        return 'index', 'dashboard'


# Custom Filter
@blueprint.app_template_filter('replace_value')
def replace_value(value, arg):
  try:
    return value.split('_')[1].replace(arg, ' ').title()
  except:
    return value.replace(arg, ' ').title()