#params
$gandivaUser = "domain\user" #changeme
$gandivaPassword = "password" #changeme
$gandivaApiUrl = "https://api-address/" #changeme

function getToken($username, $password) {
    $headers = @{
        'Content-Type' = 'x-www-form-urlencoded'
        }
    $data = @{
        'grant_type' = 'password'
        'username' = $username
        'password' = $password
        }
    $response = Invoke-RestMethod -Method Post -Headers $headers -Body $data -Uri ($gandivaApiUrl + "Token")
    return $response.access_token
}

$ggandivaApiKey = getToken $gandivaUser $gandivaPassword

$token = @{
    'Content-Type' = 'application/json'
    'Authorization' = 'Bearer '+ $ggandivaApiKey
}

function getRequestById($requestId) {
    $response = Invoke-RestMethod -Method Get -Headers $token -Uri ($gandivaApiUrl + "api/Requests/" + $requestId)
    return $response
}

getRequestById(1)
