/*
 * jsCalendar v1.4.3
 * 
 * 
 * MIT License
 * 
 * Copyright (c) 2018 Grammatopoulos Athanasios-Vasileios
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 * 
 */


/* Default Theme */
	/* General style */
		.jsCalendar * {
			margin: 0;
			padding: 0;
		}
		.jsCalendar table,
		.jsCalendar table th,
		.jsCalendar table td {
			border: 0;
		}
	/* Blue default */
		.jsCalendar table {
			background-color: #FFFFFF;
			border-collapse: collapse;
			border-radius: 4px;
			box-shadow: 0 0 2px rgba(0, 0, 0, 0.4);
			color: #000000;
			font-family: Tahoma, Geneva, sans-serif;
			margin: 5px;
		}
		.jsCalendar thead .jsCalendar-title {
			height: 40px;
			line-height: 40px;
		}
		.jsCalendar thead .jsCalendar-title-left {
			float: left;
		}
		.jsCalendar thead .jsCalendar-title-right {
			float: right;
		}
		.jsCalendar thead .jsCalendar-nav-left,
		.jsCalendar thead .jsCalendar-nav-right {
			border-radius: 10px;
			color: #999999;
			cursor: pointer;
			font-family: "Courier New", Courier, monospace;
			font-size: 12px;
			font-weight: bold;
			height: 20px;
			line-height: 20px;
			margin: 10px 8px;
			text-align: center;
			transition: color 0.2s, background-color 0.2s;
			width: 20px;
		}
		.jsCalendar thead .jsCalendar-nav-left:hover,
		.jsCalendar thead .jsCalendar-nav-right:hover {
			background-color: #E2E2E2;
			color: #000000;
		}
		.jsCalendar thead .jsCalendar-nav-left {
			float: left;
		}
		.jsCalendar thead .jsCalendar-nav-right {
			float: right;
		}
		.jsCalendar thead .jsCalendar-title-name {
			cursor: default;
			float: left;
			font-size: 18px;
			font-weight: lighter;
			padding: 0 20px;
		}
		.jsCalendar thead .jsCalendar-nav-left:after {
			content: "<";
		}
		.jsCalendar thead .jsCalendar-nav-right:after {
			content: ">";
		}
		.jsCalendar thead .jsCalendar-week-days th {
			text-shadow: 0 0 1px rgba(0, 0, 0, 0.2);
		}
		.jsCalendar thead .jsCalendar-week-days th,
		.jsCalendar tbody td {
			border-radius: 18px;
			cursor: default;
			display: inline-block;
			font-size: 12px;
			font-weight: lighter;
			height: 36px;
			line-height: 36px;
			margin: 1px 2px;
			text-align: center;
			transition: color 0.1s, background-color 0.2s;
			width: 36px;
		}
		.jsCalendar tbody td:hover {
			background-color: #E6E6E6;
		}
		.jsCalendar tbody td.jsCalendar-selected {
			background-color: #FFFFFF;
			border: 2px solid #E6E6E6;
			height: 32px;
			line-height: 32px;
			width: 32px;
		}
		.jsCalendar tbody td.jsCalendar-current {
			background-color: #52C9FF;
			border-radius: 18px;
			color: #FFFFFF;
		}
		.jsCalendar tbody td.jsCalendar-previous,
		.jsCalendar tbody td.jsCalendar-next {
			color: #CACACA;
		}
		.jsCalendar tbody td.jsCalendar-previous:hover,
		.jsCalendar tbody td.jsCalendar-next:hover {
			color: #FFFFFF;
		}

		.jsCalendar thead {
			display: block;
			margin: 4px 4px 0 4px;
		}
		.jsCalendar tbody {
			display: block;
			margin: 0 4px 4px 4px;
		}
		.jsCalendar ::-moz-selection {
			background: #83D8FF;
		}
		.jsCalendar ::selection {
			background: #83D8FF;
		}
	/* Yellow */
		.jsCalendar.yellow tbody td.jsCalendar-current {
			background-color: #FFE31B;
		}
		.jsCalendar.yellow ::-moz-selection {
			background: #FDE74C;
		}
		.jsCalendar.yellow ::selection {
			background: #FDE74C;
		}
	/* Orange */
		.jsCalendar.orange tbody td.jsCalendar-current {
			background-color: #FFB400;
		}
		.jsCalendar.orange ::-moz-selection {
			background: #FFB400;
		}
		.jsCalendar.orange ::selection {
			background: #FFB400;
		}
	/* Red */
		.jsCalendar.red tbody td.jsCalendar-current {
			background-color: #F6511D;
		}
		.jsCalendar.red ::-moz-selection {
			background: #F6511D;
		}
		.jsCalendar.red ::selection {
			background: #F6511D;
		}
	/* Green */
		.jsCalendar.green tbody td.jsCalendar-current {
			background-color: #7FB800;
		}
		.jsCalendar.green ::-moz-selection {
			background: #7FB800;
		}
		.jsCalendar.green ::selection {
			background: #7FB800;
		}


/* Material Theme */
	/* Blue default */
		.jsCalendar.material-theme table {
			border-radius: 0;
		}
		.jsCalendar.material-theme thead {
			background-color: #52C9FF;
			color: #FFFFFF;
			margin: 0;
			padding: 4px 4px 0 4px;
		}
		.jsCalendar.material-theme thead .jsCalendar-title {
			display: block;
			position: relative;
		}
		.jsCalendar.material-theme thead .jsCalendar-title-name {
			border-bottom: 1px solid rgba(255, 255, 255, 0.4);
			color: #FFFFFF;
			font-size: 16px;
			left: 15px;
			position: absolute;
			right: 15px;
			text-align: center;
		}
		.jsCalendar.material-theme thead .jsCalendar-title-left,
		.jsCalendar.material-theme thead .jsCalendar-title-right {
			position: absolute;
			z-index: 1;
		}
		.jsCalendar.material-theme thead .jsCalendar-nav-left,
		.jsCalendar.material-theme thead .jsCalendar-nav-right {
			color: #FFFFFF;
		}
		.jsCalendar.material-theme thead .jsCalendar-nav-left:hover,
		.jsCalendar.material-theme thead .jsCalendar-nav-right:hover {
			background-color: #03A9F4;
		}
		.jsCalendar.material-theme thead .jsCalendar-title-right {
			right: 0;
		}
		.jsCalendar.material-theme thead .jsCalendar-week-days th {
			font-size: 14px;
			text-shadow: none;
		}
	/* Yellow */
		.jsCalendar.material-theme.yellow thead {
			background-color: #FFE31B;
		}
		.jsCalendar.material-theme.yellow thead .jsCalendar-nav-left:hover,
		.jsCalendar.material-theme.yellow thead .jsCalendar-nav-right:hover {
			background-color: #E2CA23;
		}
	/* Orange */
		.jsCalendar.material-theme.orange thead {
			background-color: #FFB400;
		}
		.jsCalendar.material-theme.orange thead .jsCalendar-nav-left:hover,
		.jsCalendar.material-theme.orange thead .jsCalendar-nav-right:hover {
			background-color: #D49600;
		}
	/* Red */
		.jsCalendar.material-theme.red thead {
			background-color: #F6511D;
		}
		.jsCalendar.material-theme.red thead .jsCalendar-nav-left:hover,
		.jsCalendar.material-theme.red thead .jsCalendar-nav-right:hover {
			background-color: #BB3D16;
		}
	/* Green */
		.jsCalendar.material-theme.green thead {
			background-color: #7FB800;
		}
		.jsCalendar.material-theme.green thead .jsCalendar-nav-left:hover,
		.jsCalendar.material-theme.green thead .jsCalendar-nav-right:hover {
			background-color: #639000;
		}



/* Classic Theme */
	/* Blue default */
		.jsCalendar.classic-theme table,
		.jsCalendar.classic-theme thead .jsCalendar-nav-left,
		.jsCalendar.classic-theme thead .jsCalendar-nav-right,
		.jsCalendar.classic-theme thead .jsCalendar-week-days th,
		.jsCalendar.classic-theme tbody td,
		.jsCalendar.classic-theme tbody td.jsCalendar-current {
			border-radius: 0;
		}
		.jsCalendar.classic-theme thead {
			background-color: #52C9FF;
			margin: 0;
			padding: 4px 4px 0 4px;
		}
		.jsCalendar.classic-theme thead .jsCalendar-title-row,
		.jsCalendar.classic-theme thead .jsCalendar-title {
			display: block;
			width: 100%;
		}
		.jsCalendar.classic-theme thead .jsCalendar-title {
			position: relative;
		}
		.jsCalendar.classic-theme thead .jsCalendar-title-name {
			color: #FFFFFF;
			font-size: 16px;
			left: 41px;
			position: absolute;
			right: 41px;
			text-align: center;
			text-shadow: none;
		}
		.jsCalendar.classic-theme thead .jsCalendar-title-left,
		.jsCalendar.classic-theme thead .jsCalendar-title-right {
			position: absolute;
			z-index: 1;
		}
		.jsCalendar.classic-theme thead .jsCalendar-title-right {
			right: 0;
		}
		.jsCalendar.classic-theme thead .jsCalendar-nav-left,
		.jsCalendar.classic-theme thead .jsCalendar-nav-right {
			color: #FFFFFF;
			text-shadow: none;
		}
		.jsCalendar.classic-theme thead .jsCalendar-nav-left:hover,
		.jsCalendar.classic-theme thead .jsCalendar-nav-right:hover {
			background-color: #03A9F4;
		}
		.jsCalendar.classic-theme thead .jsCalendar-week-days {
			background-color: #FFFFFF;
			display: block;
			margin: 0 -4px;
		}
		.jsCalendar.classic-theme thead .jsCalendar-week-days th {
			font-size: 10px;
			height: 20px;
			line-height: 20px;
			text-shadow: none;
		}
		.jsCalendar.classic-theme tbody td {
			border-left: 1px solid #DADADA;
			border-top: 1px solid #DADADA;
			margin: -1px 0 0 -1px;
			padding: 1px 1px 0 1px;
			width: 38px;
		}
		.jsCalendar.classic-theme tbody {
			margin: 0;
		}
		.jsCalendar.classic-theme tbody td.jsCalendar-selected{
			background-color: #CCEFFF;
			border-bottom: 0;
			border-left: 1px solid #DADADA;
			border-right: 0;
			border-top: 1px solid #DADADA;
			height: 36px;
			line-height: 36px;
		}
		.jsCalendar.classic-theme tbody td.jsCalendar-current.jsCalendar-selected{
			background-color: #52C9FF; 
			text-shadow: 0 0 3px #000000;
		}
	/* Yellow */
		.jsCalendar.classic-theme.yellow thead {
			background-color: #FFE31B;
		}
		.jsCalendar.classic-theme.yellow thead .jsCalendar-nav-left:hover,
		.jsCalendar.classic-theme.yellow thead .jsCalendar-nav-right:hover {
			background-color: #E2CA23;
		}
	/* Orange */
		.jsCalendar.classic-theme.orange thead {
			background-color: #FFB400;
		}
		.jsCalendar.classic-theme.orange thead .jsCalendar-nav-left:hover,
		.jsCalendar.classic-theme.orange thead .jsCalendar-nav-right:hover {
			background-color: #D49600;
		}
	/* Red */
		.jsCalendar.classic-theme.red thead {
			background-color: #F6511D;
		}
		.jsCalendar.classic-theme.red thead .jsCalendar-nav-left:hover,
		.jsCalendar.classic-theme.red thead .jsCalendar-nav-right:hover {
			background-color: #BB3D16;
		}
	/* Green */
		.jsCalendar.classic-theme.green thead {
			background-color: #7FB800;
		}
		.jsCalendar.classic-theme.green thead .jsCalendar-nav-left:hover,
		.jsCalendar.classic-theme.green thead .jsCalendar-nav-right:hover {
			background-color: #639000;
}