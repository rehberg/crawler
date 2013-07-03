##*****************************************************************************
## TITLE:                   Two Leg Software - Surf and Collect URLs
## FILENAME:                geturls.pl
## RELATED FILE(S)          none
## PREPARED FOR:            Personal project
## PROGRAMMER(S):           Ben Rehberg
## DEVELOPMENT DATE:        July 2, 2013 (initial)
## COMPILER USED:           Strawberry Perl - Perl v5.16.3 
## TARGET PLATFORM:         Any Perl 5
##=============================================================================
##                            REVISION HISTORY
##    List revisions made to the Program
##
##  DATE		PROGRAMMER			DESCRIPTION OF CHANGES MADE
##	7/2/2013	Ben Rehberg			Initial conception. Changes will be tracked
##									with Git.
##*****************************************************************************
##             CLASSES, FREE, AND FRIEND FUNCTIONS IMPLEMENTED
##
##
##*****************************************************************************
##                               CONSTANTS
##*****************************************************************************
##                  STANDARD AND USER DEFINED INCLUDES
##*****************************************************************************
##             Definition of member functions for class
##*****************************************************************************
##
##
##    Begin program code
use LWP;

my $url = 'http://www.benrehberg.com/';

my $browser = LWP::UserAgent->new;
my $response = $browser->get($url);
die "Can't get $url -- ", $response->status_line
	unless $response->is_success;
	
die "Expecting HTML, got ", $response->content_type
	unless $response->content_type eq 'text/html';

print $response->content;