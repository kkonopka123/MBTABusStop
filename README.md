# MBTABusStop

## Introduction
 The intention of this application is to create a simple application that allows you to get automated times for your bus line stop for MBTA in Boston, MA. The idea is to have this app deployed on to RaspberryPI, which will be connected to monitor.  The app will be able to turn on/off the monitor depending on the settings. This application is purely for personal usage. I decided to add the flask framework to this project as learning opportunity for me. 
 
## Problem Statement
Every morning, I am running around getting ready for work. I want to be able to see when is the next bus coming. I want this to be fully automated, so that I do not have to start anything, press any buttons, or even pull out my phone.

## Requirements
* Automated time updates for a specific bus line
* A scheduler/timer that will activate the application automatically

## Solution
* Requesting data from the [MBTA API](https://www.mbta.com/developers/v3-api) to pull the information about stop
* Flask framework to serve the connect to the users browsers 
* Request python module to connect with MBTA API through REST requests
* Scheduler/timer - TBD
* Controlling the monitor display - TBD

